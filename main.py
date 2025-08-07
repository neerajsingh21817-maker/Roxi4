from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, ContextTypes
from send_movie_files import send_all_movies
import config

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    chat_id = update.effective_chat.id
    await send_all_movies(context.bot, chat_id)

def main():
    app = ApplicationBuilder().token(config.BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.run_polling()

if __name__ == '__main__':
    main()
