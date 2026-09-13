import asyncio
import httpx
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

MCP_URL = "http://agent-reach-linkedin.railway.internal:8000/mcp"

async def main():
    async with httpx.AsyncClient(headers={"Host": "localhost:8000"}) as client:
        async with streamablehttp_client(MCP_URL, http_client=client) as (read_stream, write_stream, _):
            async with ClientSession(read_stream, write_stream) as session:
                await session.initialize()
                result = await session.call_tool("search_jobs", {"keywords": "Java Spring Boot", "location": "Morocco", "max_pages": 1})
                print("LINKEDIN_PROBE_OK", flush=True)
                print(str(result)[:3000], flush=True)

asyncio.run(main())
