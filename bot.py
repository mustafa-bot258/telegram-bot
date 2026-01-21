from telegram import Update
from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes

TOKEN = "PUT_YOUR_BOT_TOKEN_HERE"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "هلا 👋\n"
        "أنا بوت رد تلقائي.\n"
        "اكتب سؤالك وأنا أجاوبك 😉"
    )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "مرحبا" in text or "هلو" in text:
        reply = "أهلين وسهلين 🌹"
    elif "منو انت" in text:
        reply = "أنا بوت أرد بدال صاحب الحساب 🤖"
    elif "شلونك" in text:
        reply = "تمام الحمدلله، انت شلونك؟ 😊"
    elif "مساعدة" in text:
        reply = "اكتب سؤالك وأنا أحاول أساعدك"
    else:
        reply = "وصلني سؤالك 👍 راح يتم الرد بأقرب وقت"

    await update.message.reply_text(reply)

def main():
    app = ApplicationBuilder().token(TOKEN).build()

    app.add_handler(CommandHandler("start", start))
    app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

    print("Bot is running...")
    app.run_polling()

if __name__ == "__main__":
    main()
