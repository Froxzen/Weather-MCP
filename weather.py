from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialise FastMCP server
mcp = FastMCP("weather")

# Constants
NSW_API_BASE = "https://api.weather.gov"
USER_AGENT = "weather-app/1.0"