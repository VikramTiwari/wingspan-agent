import warnings
import logging

from dotenv import load_dotenv
from src.connectors.bot_telegram import run_telegram_bot

# Configure environment and logging
load_dotenv(verbose=True)
warnings.filterwarnings("ignore")
logging.basicConfig(level=logging.ERROR)

print("Libraries imported.")


run_telegram_bot()

