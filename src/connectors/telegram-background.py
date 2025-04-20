import logging
import os

from dotenv import load_dotenv
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler, MessageHandler, filters
from src.main import call_agent_async, runner, APP_NAME

load_dotenv()

TELEGRAM_TOKEN = os.getenv('TELEGRAM_TOKEN')

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

logger = logging.getLogger(__name__)

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="Welcome to Wingspan bot at Shrek Cafe!")

async def handle_message(update: Update, context: ContextTypes.DEFAULT_TYPE):
    # Log message details
    logger.info(f"Message from {update.effective_user.username} (ID: {update.effective_user.id})")
    logger.info(f"Chat ID: {update.effective_chat.id}")
    logger.info(f"Message text: {update.message.text}")

    # Create a unique session ID for this chat
    session_id = f"telegram_{update.effective_chat.id}"
    user_id = f"telegram_{update.effective_user.id}"

    try:
        session = runner.session_service.get_session(
            app_name=APP_NAME,
            user_id=user_id,
            session_id=session_id
        )
        if session is None:
            # Create a new session if it doesn't exist
            session = runner.session_service.create_session(
                app_name=APP_NAME,
                user_id=user_id,
                session_id=session_id
            )
            logger.info(f"New session created: {session}")

        # Call the agent and get the response
        response = await call_agent_async(
            query=update.message.text,
            runner=runner,
            user_id=user_id,
            session_id=session_id
        )

        # Send the response back to the user
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text=response
        )
    except Exception as e:
        logger.error(f"Error processing message: {str(e)}")
        await context.bot.send_message(
            chat_id=update.effective_chat.id,
            text="Sorry, I encountered an error processing your message."
        )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TELEGRAM_TOKEN).build()

    start_handler = CommandHandler('start', start)
    message_handler = MessageHandler(filters.TEXT & ~filters.COMMAND, handle_message)

    application.add_handler(start_handler)
    application.add_handler(message_handler)

    application.run_polling()
