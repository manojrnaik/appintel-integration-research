
import os
from dotenv import load_dotenv
from composio import Composio

load_dotenv()

if not os.getenv("COMPOSIO_API_KEY"):
    raise RuntimeError("Add COMPOSIO_API_KEY to .env first")

composio = Composio()

session = composio.sessions.create(
    user_id="appintel-research",
    mcp=True
)

print("Composio MCP endpoint:")
print(session.mcp.url)

print("MCP authentication headers:")
print(session.mcp.headers)
