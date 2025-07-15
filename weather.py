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
async def make_nws_request(url: str) -> dict[str, Any] | None:
	"""Make a request to the NSW API with proper error handling"""
	headers = {
		"User-Agent": USER_AGENT,
		"Accept": "application/geo+json"
	}
	async with httpx.AsyncClient() as client:
		try:
			response = await client.get(url, headers=headers, timeout=30.0)
			response.raise_for_status()
			return response.json()
		except Exception:
			return None