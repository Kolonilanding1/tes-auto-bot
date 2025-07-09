from telegram import InlineKeyboardButton, InlineKeyboardMarkup, Update
from telegram.ext import ApplicationBuilder, CommandHandler, CallbackQueryHandler, ContextTypes
import logging
import asyncio

logging.basicConfig(level=logging.INFO)

API_TOKEN = "8110875332:AAG33TTd_CnmC_eFi58VhbNCSHL8A_EwfXA"

async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    keyboard = [[InlineKeyboardButton("Klik saya", callback_data="clicked")]]
    reply_markup = InlineKeyboardMarkup(keyboard)
    await update.message.reply_text("Halo! Silakan tekan tombol di bawah ini:", reply_markup=reply_markup)

async def button_handler(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await query.edit_message_text(text=f"Tombol berhasil diklik oleh {query.from_user.first_name}!")

async def main():
    app = ApplicationBuilder().token(API_TOKEN).build()
    app.add_handler(CommandHandler("start", start))
    app.add_handler(CallbackQueryHandler(button_handler))
    await app.run_polling()

if __name__ == "__main__":
    asyncio.run(main())
