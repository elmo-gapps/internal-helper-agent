from google.adk.agents import Agent

from .hubspot_agent.agent import hubspot_agent
from .severa_agent.agent import severa_agent

root_agent = Agent(
    name="root_agent",
    model="gemini-2.5-flash",
    global_instruction="""You are a helpful virtual assistant for Elmo AI company.""",
    instruction="""You are the main assistant and your job is to help users with their tasks.""",
    sub_agents=[hubspot_agent, severa_agent],
)
