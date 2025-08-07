from telegram import InlineKeyboardButton, InlineKeyboardMarkup
import config

def get_caption_and_buttons():
    caption = (
        "🎬 <b>Wednesday – Season 2 Episode 1</b>\n"
        "🎞️ <b>Language:</b> Hindi + English\n"
        "📺 <b>Subtitles:</b> English\n"
        "📤 <b>Uploaded on:</b> @rozimovie\n\n"
        "📁 <b>Choose your quality below:</b>"
    )

    buttons = [
        [
            InlineKeyboardButton("📦 480p (~260MB)", url=config.ARLINKS_URL),
        ],
        [
            InlineKeyboardButton("📦 720p (~276MB)", url=config.ARLINKS_URL)
        ]
    ]

    return caption, InlineKeyboardMarkup(buttons)
