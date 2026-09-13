import asyncio
from mcp import ClientSession
from mcp.client.streamable_http import streamablehttp_client

MCP_URL = "http://agent-reach-linkedin.railway.internal:8000/mcp"

async def main():
    async with streamablehttp_client(MCP_URL) as (read_stream, write_stream, _):
        async with ClientSession(read_stream, write_stream) as session:
            await session.initialize()
            result = await session.call_tool("search_jobs", {"keywords": "Java Spring Boot", "location": "Morocco", "max_pages": 1})
            print("LINKEDIN_PROBE_OK")
            print(str(result)[:4000])

asyncio.run(main())
