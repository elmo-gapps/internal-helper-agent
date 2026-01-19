from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

from google.genai.types import GenerateContentConfig

import os

from .prompts import INSTRUCTION


def hubspot_agent() -> Agent:
    """Returns the hubspot agent."""
    hubspot_access_token = os.getenv("HUBSPOT_ACCESS_TOKEN")
    if not hubspot_access_token:
        raise ValueError("HUBSPOT_ACCESS_TOKEN environment variable not set.")

    return Agent(
        name="hubspot_agent",
        model="gemini-2.5-flash",
        description=(
            "Agent to answer questions about HubSpot."
        ),
        instruction=(INSTRUCTION),
        output_key="hubspot_results",
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
                            "PRIVATE_APP_ACCESS_TOKEN": hubspot_access_token
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
