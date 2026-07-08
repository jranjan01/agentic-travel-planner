from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioServerParameters

travel_mcp = MCPToolset(
    connection_params=StdioServerParameters(
        command="uv",
        args=[
            "run",
            "python",
            "/Users/<....>/workplace/travel-mcp-server/server.py",
        ],
    )
)
