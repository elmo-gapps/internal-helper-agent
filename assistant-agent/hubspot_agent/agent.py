from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

from google.genai.types import GenerateContentConfig

import os

from .prompts import INSTRUCTION

HUBSPOT_ACCESS_TOKEN = os.getenv("HUBSPOT_ACCESS_TOKEN")

hubspot_agent = Agent(
    name="hubspot_agent",
    model="gemini-2.5-flash",
    description=(
        "Agent to answer questions about HubSpot."
    ),
    instruction=(INSTRUCTION),
    tools=[
        MCPToolset(
            connection_params=StdioConnectionParams(
                server_params=StdioServerParameters(
                    command='npx',
                    args=[
                        "-y",
                        "@hubspot/mcp-server"
                    ],
                    # Pass the API key as an environment variable to the npx process
                    # This is how the MCP server for Google Maps expects the key.
                    env={
                        "PRIVATE_APP_ACCESS_TOKEN": HUBSPOT_ACCESS_TOKEN
                    }
                ),
            ),
            # You can filter for specific Maps tools if needed:
            # tool_filter=['get_directions', 'find_place_by_id']
        )
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.0, top_p=0.5
    )
)
