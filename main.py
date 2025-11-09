from fastmcp import FastMCP

# Initialize MCP app
mcp = FastMCP("Math Operations MCP")

@mcp.tool
def add(a: float, b: float) -> float:
    """Add two numbers."""
    return a + b

@mcp.tool
def subtract(a: float, b: float) -> float:
    """Subtract two numbers."""
    return a - b

if __name__ == "__main__":
    mcp.run(transport='http', host='0.0.0.0', port=8000)
