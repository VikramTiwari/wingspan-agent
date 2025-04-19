from google.adk.agents import Agent

from src.agents.bird_facts import bird_facts_agent
from src.agents.bird_image_recognition import bird_image_recognition_agent
from src.tools.get_bird import get_bird

AGENT_MODEL='gemini-2.0-flash-lite'
AGENT_NAME="wingspan_agent_v1"
AGENT_DESCRIPTION="The main coordinator agent for the Wingspan app. Handles user queries and coordinates other agents."
AGENT_INSTRUCTIONS=[
    "You are a helpful assistant that can help with identifying bird from images and providing facts about birds.",
    "You have specialized sub-agents for different tasks.",
    "1. bird_facts_agent: Provides facts about birds.",
    "2. bird_image_recognition_agent: Identifies birds from images.",
    "You can also ask the user clarifying questions if needed.",
    "For anything unrelated to birds, you should say 'I can only help with birds.'",
]
AGENT_TOOLS=[get_bird]
AGENT_SUBAGENTS=[
    bird_facts_agent,
    bird_image_recognition_agent
]

wingspan_agent = None

try:
    wingspan_agent = Agent(
        name=AGENT_NAME,
        description=AGENT_DESCRIPTION,
        instruction="\n".join(AGENT_INSTRUCTIONS),
        model=AGENT_MODEL,
        tools=AGENT_TOOLS,
        sub_agents=AGENT_SUBAGENTS,
    )
    print(f"Root Agent '{AGENT_NAME}' created successfully with sub-agents {[sub_agent.name for sub_agent in AGENT_SUBAGENTS]}.")
except Exception as e:
    print(f"Error creating root agent '{AGENT_NAME}': {e}")
