from google.adk.runners import Runner
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.genai import types # For creating message Content/Parts

from src import wingspan_agent

APP_NAME = "wingspan"

# Initialize services
session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()

def create_new_session(user_id, session_id):
    """Create a new session for the given user and session ID."""
    session = session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id
    )
    print(f"Session created: App='{APP_NAME}', User='{user_id}', Session='{session_id}'")
    return session

def get_session(user_id, session_id):
    """Retrieve an existing session for the given user and session ID."""
    return session_service.get_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id
    )

async def call_agent_async(query: str, user_id, session_id):
    """Sends a query to the agent and returns the final response."""
    print(f"\n>>> User ${user_id}-${session_id} Query: {query}")

    # Prepare the user's message in ADK format
    content = types.Content(role='user', parts=[types.Part(text=query)])
    final_response_text = "Agent did not produce a final response."

    async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
        if event.is_final_response():
            if event.content and event.content.parts:
                final_response_text = event.content.parts[0].text
            elif event.actions and event.actions.escalate:
                final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
            break
    print(f"<<< Agent Response: {final_response_text}")
    return final_response_text

# Runner orchestrates the agent execution loop.
runner = Runner(
    agent=wingspan_agent,
    app_name=APP_NAME,  # Associates runs with our app
    session_service=session_service,  # Uses our session manager
    artifact_service=artifact_service,  # Uses our artifact manager
)
print(f"Runner created for agent '{runner.agent.name}'.")

