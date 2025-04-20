import pathlib

from google.adk.evaluation.agent_evaluator import AgentEvaluator

import dotenv
import pytest


@pytest.fixture(scope='session', autouse=True)
def load_env():
    dotenv.load_dotenv()


def test_eval_full_conversation():
    """Test the agent's basic ability on a few examples."""
    AgentEvaluator.evaluate(
       agent_module="src",
       eval_dataset_file_path_or_dir=str(pathlib.Path(__file__).parent / "data/evalset-initial.test.json"),
       num_runs=1,
    )
