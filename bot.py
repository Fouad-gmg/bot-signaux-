import os
import random
import logging
from telegram import Update
from telegram.ext import ApplicationBuilder, ContextTypes, CommandHandler

logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

TOKEN = "924383975:AAEmYaY7z7b-jRp0osaZ2xfgyGhqTYmoDds"

async def send_signal(update: Update, context: ContextTypes.DEFAULT_TYPE):
    actifs = ["EUR/USD (OTC)", "GBP/USD", "EUR/JPY", "Bitcoin (BTC)"]
    actif_choisi = random.choice(actifs)
    direction = random.choice(["🟢 ACHAT (CALL / HAUSSE)", "🔴 VENTE (PUT / BAISSE)"])
    duree = random.choice(["1 minute", "5 minutes"])
    
    message = (
        f"🚨 **NOUVEAU SIGNAL DE TRADING** 🚨\n\n"
        f"📊 **Actif :** `{actif_choisi}`\n"
        f"📈 **Direction :** {direction}\n"
        f"⏱ **Expiration :** {duree}\n"
        f"⚠️ *Gérez bien votre capital.*\n\n"
        f"🤖 *Signaux Trading Pro Bot*"
    )
    
    await context.bot.send_message(
        chat_id=update.effective_chat.id, 
        text=message, 
        parse_mode="Markdown"
    )

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.message.reply_text(
        "👋 Bienvenue sur ton bot de signaux ! "
        "Tape la commande /signal pour générer un nouveau signal."
    )

if __name__ == '__main__':
    application = ApplicationBuilder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))
    application.add_handler(CommandHandler("signal", send_signal))

    print("Le bot est en ligne et à l'écoute...")
    application.run_polling()
