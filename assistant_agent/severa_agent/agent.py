from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

from google.genai.types import GenerateContentConfig

import os

from .prompts import INSTRUCTION


def severa_agent() -> Agent:
    """Returns the severa agent."""
    severa_client_id = os.getenv("SEVERA_CLIENT_ID")
    severa_client_secret = os.getenv("SEVERA_CLIENT_SECRET")
    if not severa_client_id or not severa_client_secret:
        raise ValueError(
            "SEVERA_CLIENT_ID and SEVERA_CLIENT_SECRET environment variables not set."
        )

    return Agent(
        name="severa_agent",
        model="gemini-2.5-flash",
        description=(
            "Agent to answer questions about Severa."
        ),
        instruction=(INSTRUCTION),
        tools=[
            MCPToolset(
                connection_params=StdioConnectionParams(
                    server_params=StdioServerParameters(
                        command="python",
                        args=["-m", "mcp-severa.server"],
                        timeout=15,
                        env={
                            "SEVERA_CLIENT_ID": severa_client_id,
                            "SEVERA_CLIENT_SECRET": severa_client_secret,
                        }
                    )
                ),
            )
        ],
        generate_content_config=GenerateContentConfig(
            temperature=0.0, top_p=0.5
        )
    )
