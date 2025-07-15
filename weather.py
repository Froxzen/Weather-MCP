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

# _Helper Functions_
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

def format_alert(feature: dict) -> str:
	"""Format an alert feature into a readable string"""
	props = feature["properties"]
	return f"""
		Event: {props.get('event', 'Unknown')}
		Area: {props.get('areaDesc', 'Unknown')}
		Severity: {props.get('severity', 'Unknown')}
		Description: {props.get('description', 'No description available')}
		Instructions: {props.get('instruction', 'No specific instructions provided')}
	"""

@mcp.tool()
async def get_alerts(state: str) -> str:
	"""
		Get weather alerts for a US state.

		Args:
			state: Two-letter US state code
	"""
	url = f"{NSW_API_BASE}/alerts/active/area/{state}"
	data = await make_nws_request(url)

	if not data or "features" not in data:
		return "Unable to fetch alerts or no alerts found."
	
	if not data["features"]:
		return "No active alerts for this state."
	
	alerts = [format_alert(feature) for feature in data["features"]]
	return "\n---\n".join(alerts)