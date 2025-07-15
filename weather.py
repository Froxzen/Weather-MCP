from typing import Any
import httpx
from mcp.server.fastmcp import FastMCP

# Initialise FastMCP server
mcp = FastMCP("weather")

# _Constants_
# Base URL for the National Weather Service (NWS) API 
NSW_API_BASE = "https://api.weather.gov"
# A string that identifies your application when making HTTP requests
USER_AGENT = "weather-app/1.0"

# Helper Functions
async def make_nws