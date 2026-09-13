import json
import os
import sys
import urllib.parse
import urllib.request
from datetime import datetime, timezone

BASE = os.environ.get("GATEWAY_URL", "https://linkedin-gateway-production-a51c.up.railway.app").rstrip("/")
TOKEN = os.environ.get("GATEWAY_API_KEY", "")
MAX_LOG_CHARS = 20000

JOB_QUERIES = [
    ("Software Engineer", "Morocco"),
    ("Backend Engineer", "Morocco"),
    ("Full Stack Engineer", "Morocco"),
    ("Java Developer", "Morocco"),
    ("Software Engineer", "Remote"),
    ("Backend Engineer", "Remote"),
    ("Software Engineer", "United Arab Emirates"),
    ("Software Engineer", "Saudi Arabia"),
]

POST_QUERIES = [
    "software engineer hiring Morocco",
    "java hiring Morocco",
    "remote software engineer EMEA",
    "visa sponsorship software engineer",
]

HIRING_TERMS = [
    "hiring", "we're hiring", "we are hiring", "recruit", "recrut",
    "job opening", "vacancy", "opportunity", "software engineer",
    "backend engineer", "full stack", "fullstack", "java developer",
    "spring boot", "react developer", "developer", "emploi", "poste",
]


def request_json(path: str, params: dict | None = None):
    if not TOKEN:
        raise RuntimeError("GATEWAY_API_KEY is not configured")
    query = ""
    if params:
        query = "?" + urllib.parse.urlencode(params)
    url = f"{BASE}/v1/{urllib.parse.quote(TOKEN, safe='')}{path}{query}"
    req = urllib.request.Request(url, headers={"User-Agent": "linkedin-scanner/1.0"})
    with urllib.request.urlopen(req, timeout=180) as resp:
        data = resp.read().decode("utf-8", errors="replace")
    try:
        return json.loads(data)
    except json.JSONDecodeError:
        return data


def normalize_items(value):
    if isinstance(value, str):
        text = value.strip()
        if text.startswith("{") or text.startswith("["):
            try:
                return normalize_items(json.loads(text))
            except Exception:
                return [value]
        return [value]
    if isinstance(value, list):
        out = []
        for item in value:
            out.extend(normalize_items(item))
        return out
    if isinstance(value, dict):
        for key in ("results", "jobs", "posts", "items", "data"):
            if isinstance(value.get(key), list):
                return value[key]
        return [value]
    return [value]


def bounded(value, limit=MAX_LOG_CHARS):
    text = json.dumps(value, ensure_ascii=False, default=str)
    if len(text) <= limit:
        return text
    return text[:limit] + "...<truncated>"


def emit(prefix: str, payload):
    print(prefix + " " + bounded(payload), flush=True)


def looks_like_hiring(item) -> bool:
    text = json.dumps(item, ensure_ascii=False, default=str).lower()
    return any(term in text for term in HIRING_TERMS)


def main():
    scan_at = datetime.now(timezone.utc).isoformat()
    emit("LINKEDIN_SCAN_START", {"scan_at": scan_at})
    errors = 0

    for keywords, location in JOB_QUERIES:
        try:
            result = request_json(
                "/jobs",
                {
                    "keywords": keywords,
                    "location": location,
                    "max_pages": 1,
                    "date_posted": "past-week",
                },
            )
            emit(
                "LINKEDIN_SCAN_JOBS",
                {
                    "scan_at": scan_at,
                    "keywords": keywords,
                    "location": location,
                    "items": normalize_items(result)[:30],
                },
            )
        except Exception as exc:
            errors += 1
            emit("LINKEDIN_SCAN_ERROR", {"scan_at": scan_at, "kind": "jobs", "keywords": keywords, "location": location, "error": f"{type(exc).__name__}: {exc}"})

    for keywords in POST_QUERIES:
        try:
            result = request_json(
                "/posts",
                {"keywords": keywords, "recency": "past-week", "max_pages": 1},
            )
            emit(
                "LINKEDIN_SCAN_POSTS",
                {"scan_at": scan_at, "keywords": keywords, "items": normalize_items(result)[:30]},
            )
        except Exception as exc:
            errors += 1
            emit("LINKEDIN_SCAN_ERROR", {"scan_at": scan_at, "kind": "posts", "keywords": keywords, "error": f"{type(exc).__name__}: {exc}"})

    try:
        feed = request_json("/feed")
        matches = [item for item in normalize_items(feed) if looks_like_hiring(item)][:30]
        emit("LINKEDIN_SCAN_FEED", {"scan_at": scan_at, "matched_count": len(matches), "items": matches})
    except Exception as exc:
        errors += 1
        emit("LINKEDIN_SCAN_ERROR", {"scan_at": scan_at, "kind": "feed", "error": f"{type(exc).__name__}: {exc}"})

    try:
        saved = request_json("/saved-jobs")
        emit("LINKEDIN_SCAN_SAVED_JOBS", {"scan_at": scan_at, "items": normalize_items(saved)[:30]})
    except Exception as exc:
        errors += 1
        emit("LINKEDIN_SCAN_ERROR", {"scan_at": scan_at, "kind": "saved_jobs", "error": f"{type(exc).__name__}: {exc}"})

    emit("LINKEDIN_SCAN_DONE", {"scan_at": scan_at, "status": "ok" if errors == 0 else "completed_with_errors", "errors": errors})
    return 0 if errors == 0 else 1


if __name__ == "__main__":
    sys.exit(main())
