from telegram.ext import ApplicationBuilder, CommandHandler, MessageHandler, filters, ContextTypes
from telegram import Update

TOKEN =8196425325:AAEDo6h6rc0fJszPGEKc8_DZtbPAah3DJeg

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 هلا!\n"
        "أنا بوت يرد تلقائيًا بدل صاحبي 🤖\n"
        "اكتب سؤالك وأنا أجاوبك 😉"
    )

async def auto_reply(update: Update, context: ContextTypes.DEFAULT_TYPE):
    text = update.message.text.lower()

    if "هلو" in text or "مرحبا" in text:
        reply = "🌹 أهلين وسهلين"
    elif "منو انت" in text:
        reply = "🤖 أنا بوت يرد بدل صاحب الحساب"
    elif "شلونك" in text:
        reply = "😊 تمام الحمدلله، إنت شلونك؟"
    else:
        reply = "📩 وصلت رسالتك، راح يرد عليك صاحب الحساب بأقرب وقت"

    await update.message.reply_text(reply)

app = ApplicationBuilder().token(TOKEN).build()

app.add_handler(CommandHandler("start", start))
app.add_handler(MessageHandler(filters.TEXT & ~filters.COMMAND, auto_reply))

app.run_polling()
