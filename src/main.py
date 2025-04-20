import os
import asyncio

from dotenv import load_dotenv
from google.adk.agents import Agent
from google.adk.models.lite_llm import LiteLlm # For multi-model support
from google.adk.sessions import InMemorySessionService
from google.adk.artifacts import InMemoryArtifactService
from google.adk.runners import Runner
from enum import Enum
from google.genai import types # For creating message Content/Parts

load_dotenv(verbose=True)

import warnings

from src.agents.wingspan import wingspan_agent

warnings.filterwarnings("ignore")

import logging
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")

session_service = InMemorySessionService()
artifact_service = InMemoryArtifactService()

APP_NAME = "wingspan"


def create_new_session(user_id, session_id):
    # Create the specific session where the conversation will happen
    session = session_service.create_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id
    )
    print(f"Session created: App='{APP_NAME}', User='{user_id}', Session='{session_id}'")

    return session

def get_session(user_id, session_id):
    return session_service.get_session(
        app_name=APP_NAME,
        user_id=user_id,
        session_id=session_id
    )

# --- Runner ---
# Runner orchestrates the agent execution loop.
runner = Runner(
    agent=wingspan_agent,
    app_name=APP_NAME,   # Associates runs with our app
    session_service=session_service, # Uses our session manager
    artifact_service=artifact_service, # Uses our artifact manager
)
print(f"Runner created for agent '{runner.agent.name}'.")


async def call_agent_async(query: str, runner, user_id, session_id):
  """Sends a query to the agent and prints the final response."""
  print(f"\n>>> User ${user_id}-${session_id} Query: {query}")

  # Prepare the user's message in ADK format
  content = types.Content(role='user', parts=[types.Part(text=query)])

  final_response_text = "Agent did not produce a final response." # Default

  # run_async executes the agent logic and yields Events.
  # We iterate through events to find the final answer.
  async for event in runner.run_async(user_id=user_id, session_id=session_id, new_message=content):
      # print(f"  [Event] Author: {event.author}, Type: {type(event).__name__}, Final: {event.is_final_response()}, Content: {event.content}")

      if event.is_final_response():
          if event.content and event.content.parts:
             # Assuming text response in the first part
             final_response_text = event.content.parts[0].text
          elif event.actions and event.actions.escalate: # Handle potential errors/escalations
             final_response_text = f"Agent escalated: {event.error_message or 'No specific message.'}"
          # Add more checks here if needed (e.g., specific error codes)
          break # Stop processing events once the final response is found

  print(f"<<< Agent Response: {final_response_text}")
  return final_response_text


