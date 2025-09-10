from google.adk.agents import Agent
from google.adk.tools.mcp_tool.mcp_toolset import MCPToolset, StdioConnectionParams, StdioServerParameters

from google.genai.types import GenerateContentConfig

import os

from .prompts import INSTRUCTION

SEVERA_CLIENT_ID = os.getenv("SEVERA_CLIENT_ID")
SEVERA_CLIENT_SECRET = os.getenv("SEVERA_CLIENT_SECRET")

severa_agent = Agent(
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
                        "SEVERA_CLIENT_ID": SEVERA_CLIENT_ID,
                        "SEVERA_CLIENT_SECRET": SEVERA_CLIENT_SECRET
                    }
                )
            ),
        )
    ],
    generate_content_config=GenerateContentConfig(
        temperature=0.0, top_p=0.5
    )
)
