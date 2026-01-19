from google.adk.agents import Agent

from .hubspot_agent.agent import hubspot_agent
from .severa_agent.agent import severa_agent
from .google_search.agent import search_agent
from .prompts import GLOBAL_INSTRUCTION, INSTRUCTION

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    global_instruction=GLOBAL_INSTRUCTION,
    instruction=INSTRUCTION,
    sub_agents=[hubspot_agent(), severa_agent()]
)
