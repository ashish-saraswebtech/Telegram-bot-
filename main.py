from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import Application, CommandHandler, CallbackQueryHandler, ContextTypes

# ===================== CONFIG =====================
BOT_TOKEN = "8871902848:AAE4UlJT_dpPcbhvM9SCwZJ2UqH-mrKxlWs"
CONTACT = "@Ashish072304"

CHANNELS = {
    "web": {
        "name": "📁 Web Development",
        "link": "https://t.me/FinalYearWebProjects"
    },
    "app": {
        "name": "📱 Mobile App",
        "link": "https://t.me/FinalYearAppProjects"
    },
    "aiml": {
        "name": "🤖 AI / ML",
        "link": "https://t.me/FinalYearAIMLProjects"
    },
    "python": {
        "name": "🐍 Python",
        "link": "https://t.me/FinalYearPythonProjects"
    },
    "ds": {
        "name": "📊 Data Science",
        "link": "https://t.me/+coCpafJxHAtlODY1"
    },
}
# ==================================================


async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [
        [InlineKeyboardButton(CHANNELS["web"]["name"], callback_data="web")],
        [InlineKeyboardButton(CHANNELS["app"]["name"], callback_data="app")],
        [InlineKeyboardButton(CHANNELS["aiml"]["name"], callback_data="aiml")],
        [InlineKeyboardButton(CHANNELS["python"]["name"], callback_data="python")],
        [InlineKeyboardButton(CHANNELS["ds"]["name"], callback_data="ds")],
    ]
    reply_markup = InlineKeyboardMarkup(keyboard)

    await update.message.reply_text(
        "👋 *Welcome to Student Project Store!* 🎓\n\n"
        "We provide Final Year Projects for BCA, MCA, B.Tech & BSc CS Students.\n\n"
        "✅ Source Code\n"
        "✅ Documentation\n"
        "✅ PPT Included\n\n"
        "👇 *Select your category:*",
        parse_mode="Markdown",
        reply_markup=reply_markup
    )


async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()

    key = query.data
    if key in CHANNELS:
        channel = CHANNELS[key]
        keyboard = [
            [InlineKeyboardButton("🔗 Open Channel", url=channel["link"])],
            [InlineKeyboardButton("📲 Contact to Order", url=f"https://t.me/{CONTACT.replace('@', '')}")],
            [InlineKeyboardButton("🔙 Back to Categories", callback_data="back")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            f"{channel['name']} *Projects* 🎓\n\n"
            f"Browse all available projects in our channel 👇\n\n"
            f"✅ Source Code + Documentation + PPT\n"
            f"✅ Ready-made & Custom Available\n\n"
            f"📲 *Interested? Contact us directly on Telegram!*",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )

    elif key == "back":
        keyboard = [
            [InlineKeyboardButton(CHANNELS["web"]["name"], callback_data="web")],
            [InlineKeyboardButton(CHANNELS["app"]["name"], callback_data="app")],
            [InlineKeyboardButton(CHANNELS["aiml"]["name"], callback_data="aiml")],
            [InlineKeyboardButton(CHANNELS["python"]["name"], callback_data="python")],
            [InlineKeyboardButton(CHANNELS["ds"]["name"], callback_data="ds")],
        ]
        reply_markup = InlineKeyboardMarkup(keyboard)

        await query.edit_message_text(
            "👋 *Welcome to Student Project Store!* 🎓\n\n"
            "We provide Final Year Projects for BCA, MCA, B.Tech & BSc CS Students.\n\n"
            "✅ Source Code\n"
            "✅ Documentation\n"
            "✅ PPT Included\n\n"
            "👇 *Select your category:*",
            parse_mode="Markdown",
            reply_markup=reply_markup
        )


def main():
    app = Application.builder().token(BOT_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    print("✅ Bot is running...")
    app.run_polling()


if __name__ == "__main__":
    main()
