# Import niezbędnych modułów
import logging
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, CommandHandler, Application, ContextTypes, ApplicationBuilder, CallbackQueryHandler, filters

# Twój tajny klucz dostępu do API Telegrama
API_KEY = '6991687705:AAFOkG3UbqmTSH5qOrnqyWNLMGQaaVRBWEE'

# Reakcja na wiadomość "/start"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    buttons = [
        [
            InlineKeyboardButton(text="TAK ✅", callback_data="tak"),
            InlineKeyboardButton(text="NIE ❌", callback_data="nie"),
        ]
    ]
    reply_markup = InlineKeyboardMarkup(buttons)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text="Siemka! 👋\nChciałbyś złożyć u nas zamówienie? 🇨🇳",
        reply_markup=reply_markup,
    )

# Reakcja na naciśnięcie przycisku "Tak"
async def takzakupy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text="jestem bodas i kurwi mi sie matka",
    )

# Reakcja na naciśnięcie przycisku "Nie"
async def niezakupy(update: Update, context: ContextTypes.DEFAULT_TYPE):
    query = update.callback_query
    await query.answer()
    await context.bot.send_message(
        chat_id=query.message.chat_id,
        text="to spierdalaj",
    )

# Reakcja na inne wiadomości
async def konsolaszmeges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update.message.chat.full_name} - {update.message.text} [{data_i_godzina}]")

# Reakcja na nieznane komendy
async def nieznana(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="co ty pierdolisz dziadzie jebany")
    print(f"{update.message.chat.full_name} - {update.message.text} [ta pierdolona komenda nawet nie istnieje]")

# Pobranie aktualnej daty i godziny
aktualna_data = datetime.now()
data_i_godzina = aktualna_data.strftime("%H:%M (%Y-%m-%d)")

# Uruchomienie bota
if __name__ == '__main__':
    print("Bot startuje")
    application = ApplicationBuilder().token(API_KEY).build()

    # Dodanie obsługi komend i przycisków
    start_handler = CommandHandler('start', start)
    konsola_handler = MessageHandler(filters.TEXT, konsolaszmeges)
    nieznanakomenda = MessageHandler(filters.COMMAND, nieznana)
    takzakupy_handler = CallbackQueryHandler(takzakupy, pattern="tak")
    niezakupy_handler = CallbackQueryHandler(niezakupy, pattern="nie")

    application.add_handler(start_handler)
    application.add_handler(konsola_handler)
    application.add_handler(nieznanakomenda)
    application.add_handler(takzakupy_handler)
    application.add_handler(niezakupy_handler)

    application.run_polling()
