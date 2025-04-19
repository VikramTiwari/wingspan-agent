from google.adk.agents import Agent

from src.tools.get_bird import get_bird

AGENT_MODEL='gemini-2.0-flash'
AGENT_NAME="bird_facts_agent_v1"
AGENT_DESCRIPTION="Provide facts about birds based on bird name in the query."
AGENT_INSTRUCTIONS=[
    "You are a helpful assistant that can only provide facts about birds.",
    "Identify the bird name in the user's query.",
    "If there is a bird name, you should use the get_bird tool to get facts about the bird.",
    "If there is no bird name, you should say 'I don't know'.",
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
