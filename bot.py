import os
import re
import logging
from telegram import Update
from telegram.ext import (
    ApplicationBuilder,
    CommandHandler,
    MessageHandler,
    ContextTypes,
    filters,
)

logging.basicConfig(
    format="%(asctime)s - %(name)s - %(levelname)s - %(message)s",
    level=logging.INFO,
)
logger = logging.getLogger(__name__)

BOT_TOKEN = os.environ.get("BOT_TOKEN")


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Hi! I'm Word Counter Bot.\n\n"
        "Just send me any text and I'll count:\n"
        "• Words\n"
        "• Characters (with & without spaces)\n"
        "• Sentences\n"
        "• Estimated reading time\n\n"
        "Try it now — paste some text!"
    )


async def help_command(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "Send me any message and I'll analyze it.\n"
        "Commands:\n"
        "/start - Welcome message\n"
        "/help - Show this help"
    )


def analyze_text(text: str) -> str:
    words = re.findall(r"\b\w+\b", text)
    word_count = len(words)
    char_count_with_spaces = len(text)
    char_count_no_spaces = len(text.replace(" ", "").replace("\n", ""))
    sentences = re.split(r"[.!?]+", text)
    sentence_count = len([s for s in sentences if s.strip()])
    # Average reading speed: ~200 words per minute
    reading_time_minutes = max(1, round(word_count / 200))

    return (
        f"📊 *Text Analysis*\n\n"
        f"📝 Words: {word_count}\n"
        f"🔤 Characters (with spaces): {char_count_with_spaces}\n"
        f"🔡 Characters (no spaces): {char_count_no_spaces}\n"
        f"📄 Sentences: {sentence_count}\n"
        f"⏱ Estimated reading time: ~{reading_time_minutes} min"
    )


async def count_words(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text
    result = analyze_text(text)
    await update.message.reply_markdown(result)


def main():
    if not BOT_TOKEN:
        raise RuntimeError(
            "BOT_TOKEN environment variable is not set. "
            "Set it in Railway's Variables tab."
        )

    app = ApplicationBuilder().token(BOT_TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(CommandHandler("help", help_command))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, count_words))

    logger.info("Bot is starting...")
    app.run_polling()


if __name__ == "__main__":
    main()
