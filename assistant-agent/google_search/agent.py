from google.adk.agents import Agent
from google.adk.tools import google_search
from google.adk.tools.agent_tool import AgentTool

from .prompts import INSTRUCTION

search_agent = Agent(
    name="search_agent",
    model="gemini-2.5-flash",
    description="Agent to answer questions using Google Search.",
    instruction=INSTRUCTION,
    tools=[google_search]
)

search_tool = AgentTool(search_agent)
