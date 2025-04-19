# TODO: this doesn't work yet
from google.adk.agents import Agent

from src.tools.get_bird import get_bird

AGENT_MODEL='gemini-2.0-flash-lite'
AGENT_NAME="bird_image_recognition_agent_v1"
AGENT_DESCRIPTION="Identifies a given bird from the image."
AGENT_INSTRUCTIONS=[
    "You are a helpful assistant that can identify a bird from the image.",
    "If there is no bird in the image, you should say 'No bird found'.",
    "If there is a bird in the image, you should identify the common name of the bird.",
    "You can use the tool get_bird to get the bird information.",
]
AGENT_TOOLS=[get_bird]

bird_image_recognition_agent = None

try:
    bird_image_recognition_agent = Agent(
        name=AGENT_NAME,
        description=AGENT_DESCRIPTION,
        instruction="\n".join(AGENT_INSTRUCTIONS),
        model=AGENT_MODEL,
        tools=AGENT_TOOLS,
    )
    print(f"Agent '{AGENT_NAME}' created successfully.")
except Exception as e:
    print(f"Error creating agent '{AGENT_NAME}': {e}")
