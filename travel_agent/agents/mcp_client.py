from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters
from travel_agent.config import FILE_PATH

travel_mcp = MCPToolset(
    connection_params=StdioServerParameters(
        command="uv",
        args=[
            "run",
            "python",
            FILE_PATH,
        ],
    )
)
