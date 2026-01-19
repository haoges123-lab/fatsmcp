from fastmcp import FastMCP

mcp = FastMCP("My MCP Server")


@mcp.tool
def add_number(number1, number2) -> float:
    return number1 + number2


if __name__ == "__main__":
    mcp.run()
