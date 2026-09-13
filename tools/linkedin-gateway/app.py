import os
import time
from collections import defaultdict, deque
from typing import Any

from fastapi import FastAPI, HTTPException, Query, Request
from mcp import Client

app = FastAPI(title="LinkedIn Read Gateway", version="1.0.0")

MCP_URL = os.environ.get("LINKEDIN_MCP_URL", "http://agent-reach-linkedin.railway.internal:8000/mcp")
API_KEY = os.environ.get("GATEWAY_API_KEY", "")
RATE_LIMIT_PER_MINUTE = int(os.environ.get("RATE_LIMIT_PER_MINUTE", "40"))

_ALLOWED_TOOLS = {
    "search_jobs",
    "get_job_details",
    "search_people",
    "get_person_profile",
    "search_companies",
    "get_company_profile",
    "get_company_posts",
    "get_company_employees",
    "search_posts",
    "get_feed",
    "get_saved_jobs",
}

_hits: dict[str, deque[float]] = defaultdict(deque)


def _authorize(token: str) -> None:
    if not API_KEY or token != API_KEY:
        raise HTTPException(status_code=404, detail="Not found")


def _rate_limit(request: Request) -> None:
    client = request.client.host if request.client else "unknown"
    now = time.monotonic()
    q = _hits[client]
    while q and now - q[0] > 60:
        q.popleft()
    if len(q) >= RATE_LIMIT_PER_MINUTE:
        raise HTTPException(status_code=429, detail="Rate limit exceeded")
    q.append(now)


def _normalize(result: Any) -> Any:
    structured = getattr(result, "structured_content", None)
    if structured is not None:
        return structured
    content = getattr(result, "content", None)
    if content is None:
        return str(result)
    out = []
    for item in content:
        if hasattr(item, "text"):
            out.append(item.text)
        elif hasattr(item, "model_dump"):
            out.append(item.model_dump(mode="json"))
        else:
            out.append(str(item))
    return out


async def _call(tool: str, arguments: dict[str, Any]) -> Any:
    if tool not in _ALLOWED_TOOLS:
        raise HTTPException(status_code=403, detail="Tool not allowed")
    try:
        async with Client(MCP_URL) as client:
            result = await client.call_tool(tool, arguments)
        return _normalize(result)
    except HTTPException:
        raise
    except Exception as exc:
        raise HTTPException(status_code=502, detail=f"LinkedIn MCP error: {type(exc).__name__}: {exc}") from exc


@app.get("/health")
async def health() -> dict[str, str]:
    return {"status": "ok"}


@app.get("/v1/{token}/jobs")
async def jobs(
    token: str,
    request: Request,
    keywords: str = Query(..., min_length=1, max_length=200),
    location: str | None = Query(default=None, max_length=120),
    max_pages: int = Query(default=2, ge=1, le=5),
    date_posted: str | None = Query(default=None, max_length=40),
) -> Any:
    _authorize(token)
    _rate_limit(request)
    args: dict[str, Any] = {"keywords": keywords, "max_pages": max_pages}
    if location:
        args["location"] = location
    if date_posted:
        args["date_posted"] = date_posted
    return await _call("search_jobs", args)


@app.get("/v1/{token}/job/{job_id}")
async def job_details(token: str, job_id: str, request: Request) -> Any:
    _authorize(token)
    _rate_limit(request)
    return await _call("get_job_details", {"job_id": job_id})


@app.get("/v1/{token}/posts")
async def posts(
    token: str,
    request: Request,
    keywords: str = Query(..., min_length=1, max_length=200),
    recency: str | None = Query(default="past-week", max_length=40),
    max_pages: int = Query(default=2, ge=1, le=5),
) -> Any:
    _authorize(token)
    _rate_limit(request)
    args: dict[str, Any] = {"keywords": keywords, "max_pages": max_pages}
    if recency:
        args["recency"] = recency
    return await _call("search_posts", args)


@app.get("/v1/{token}/people")
async def people(
    token: str,
    request: Request,
    keywords: str = Query(..., min_length=1, max_length=200),
    location: str | None = Query(default=None, max_length=120),
    max_pages: int = Query(default=2, ge=1, le=5),
) -> Any:
    _authorize(token)
    _rate_limit(request)
    args: dict[str, Any] = {"keywords": keywords, "max_pages": max_pages}
    if location:
        args["location"] = location
    return await _call("search_people", args)


@app.get("/v1/{token}/person/{username}")
async def person(token: str, username: str, request: Request) -> Any:
    _authorize(token)
    _rate_limit(request)
    return await _call("get_person_profile", {"linkedin_username": username, "sections": "experience,education,skills,certifications,projects,posts"})


@app.get("/v1/{token}/companies")
async def companies(
    token: str,
    request: Request,
    keywords: str = Query(..., min_length=1, max_length=200),
    max_pages: int = Query(default=2, ge=1, le=5),
) -> Any:
    _authorize(token)
    _rate_limit(request)
    return await _call("search_companies", {"keywords": keywords, "max_pages": max_pages})


@app.get("/v1/{token}/company")
async def company(token: str, request: Request, name: str = Query(..., min_length=1, max_length=150)) -> Any:
    _authorize(token)
    _rate_limit(request)
    return await _call("get_company_profile", {"company_name": name, "sections": "about,posts,jobs"})


@app.get("/v1/{token}/company-posts")
async def company_posts(token: str, request: Request, name: str = Query(..., min_length=1, max_length=150)) -> Any:
    _authorize(token)
    _rate_limit(request)
    return await _call("get_company_posts", {"company_name": name})


@app.get("/v1/{token}/company-employees")
async def company_employees(
    token: str,
    request: Request,
    name: str = Query(..., min_length=1, max_length=150),
    keywords: str | None = Query(default=None, max_length=150),
) -> Any:
    _authorize(token)
    _rate_limit(request)
    args: dict[str, Any] = {"company_name": name}
    if keywords:
        args["keywords"] = keywords
    return await _call("get_company_employees", args)


@app.get("/v1/{token}/feed")
async def feed(token: str, request: Request) -> Any:
    _authorize(token)
    _rate_limit(request)
    return await _call("get_feed", {})


@app.get("/v1/{token}/saved-jobs")
async def saved_jobs(token: str, request: Request) -> Any:
    _authorize(token)
    _rate_limit(request)
    return await _call("get_saved_jobs", {})
