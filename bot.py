# Import niezbędnych modułów
from datetime import datetime
from telegram import Update, InlineKeyboardButton, InlineKeyboardMarkup
from telegram.ext import MessageHandler, CommandHandler, Application, ContextTypes, CallbackQueryHandler, filters, ApplicationBuilder

# Twój tajny klucz dostępu do API Telegrama
API_KEY = '6991687705:AAFOkG3UbqmTSH5qOrnqyWNLMGQaaVRBWEE'

# Tekst wiadomości powitalnej
WIADOMOSC_POWITALNA = "Siemka! \nChciałbyś złożyć u nas zamówienie? 🇨🇳"

# Teksty odpowiedzi na przyciski
TAK_ODPOWIEDZ = "Super! Czy itemek, który chcesz zamówić znajduje się w katalogu?"
NIE_ODPOWIEDZ = "To spierdalaj!"

# Definicja przycisków
PRZYCISKI = [
    [
        InlineKeyboardButton(text="TAK ✅", callback_data="tak"),
        InlineKeyboardButton(text="NIE ❌", callback_data="nie"),
    ]
]

# Reakcja na wiadomość "/start"
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    reply_markup = InlineKeyboardMarkup(PRZYCISKI)
    await context.bot.send_message(
        chat_id=update.effective_chat.id,
        text=WIADOMOSC_POWITALNA,
        reply_markup=reply_markup,
    )

# Reakcja na naciśnięcie przycisku "TAK"
async def tak(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await context.bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        text=TAK_ODPOWIEDZ,
    )

# Reakcja na naciśnięcie przycisku "NIE"
async def nie(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await update.callback_query.answer()
    await context.bot.send_message(
        chat_id=update.callback_query.message.chat_id,
        text=NIE_ODPOWIEDZ,
    )

# Uruchomienie bota
if __name__ == '__main__':
    print("Bot startuje")
    application = ApplicationBuilder().token(API_KEY).build()

    # Dodanie obsługi komend i przycisków
    start_handler = CommandHandler('start', start)
    tak_handler = CallbackQueryHandler(tak, pattern="tak")
    nie_handler = CallbackQueryHandler(nie, pattern="nie")

    application.add_handler(start_handler)
    application.add_handler(tak_handler)
    application.add_handler(nie_handler)

    application.run_polling()
