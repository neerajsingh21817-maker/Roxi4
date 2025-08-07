import config

async def send_all_movies(bot, chat_id):
    for msg_id in config.MOVIE_MESSAGE_IDS:
        await bot.copy_message(
            chat_id=chat_id,
            from_chat_id=config.DELIVERY_CHANNEL,
            message_id=msg_id
        )
