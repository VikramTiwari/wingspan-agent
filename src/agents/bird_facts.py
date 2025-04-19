from google.adk.agents import Agent

from src.tools.get_bird import get_bird

AGENT_MODEL='gemini-2.0-flash-lite'
AGENT_NAME="bird_facts_agent_v1"
AGENT_DESCRIPTION="Provide facts about birds."
AGENT_INSTRUCTIONS=[
    "You are a helpful assistant that can only provide facts about birds.",
    "When a user asks about a bird, you should use the get_bird tool to get facts about the bird.",
]
AGENT_TOOLS=[get_bird]

bird_facts_agent = None

try:
    bird_facts_agent = Agent(
        name=AGENT_NAME,
        description=AGENT_DESCRIPTION,
        instruction="\n".join(AGENT_INSTRUCTIONS),
        model=AGENT_MODEL,
        tools=AGENT_TOOLS,
    )
    print(f"Agent '{AGENT_NAME}' created successfully.")
except Exception as e:
    print(f"Error creating agent '{AGENT_NAME}': {e}")
