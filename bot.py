# Zawsze to trzeba dodac, zeby program wiedzial co ty odpierdalasz.
import logging
from datetime import datetime
from telegram import Update
from telegram.ext import filters, MessageHandler, CommandHandler, Application, ContextTypes, ApplicationBuilder

# tajne haslo dostepu do twojego bota, zeby telegram w ogole wiedzial jakiego bota chcesz ruszyc

API_KEY = '6991687705:AAFOkG3UbqmTSH5qOrnqyWNLMGQaaVRBWEE'

# REAKCJE (czyli jak program ma sie zachowywac w efekcie czegostam)
async def bodas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="moja matka sie kurwi za regalami w kaufie ale udaje ze o tym nie wiem")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="cwelozo44200000")
# fajne, sam skleilem -- za kazdym razem jak ktos wysle wiadomosc to widac cala nazwe i tresc
async def konsolaszmeges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update.message.chat.full_name} - {update.message.text} [{data_i_godzina}]")
async def nieznana(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="co ty pierdolisz dziadzie jebany")
    print(f"{update.message.chat.full_name} - {update.message.text} [ta pierdolona komenda nawet nie istnieje]")

aktualna_data = datetime.now()
data_i_godzina = aktualna_data.strftime("%H:%M (%Y-%m-%d)")

# to jest mega wazne, wszystko co sie dzieje w programie musi byc podpiete pod tego if'a

if __name__ == '__main__':
    print("Bot startuje")
    application = ApplicationBuilder().token(API_KEY).build()
    
    # Tu opisujesz akcje (zeby program wiedzial kiedy i co ma robic)
    start_handler = CommandHandler('start', start)
    kutasowcy = MessageHandler(filters.Text("jajeczko"), bodas)
    bodas_handler = CommandHandler('chujek', bodas)
    konsola_handler = MessageHandler(filters.TEXT, konsolaszmeges)
    nieznanakomenda = MessageHandler(filters.COMMAND, nieznana)
    
    # deklaruje akcje (zeby program wiedzial czy tamto co pisales wczesniej jest dla beki czy na serio)
    application.add_handler(start_handler)
    application.add_handler(bodas_handler)
    application.add_handler(kutasowcy)
    application.add_handler(konsola_handler)
    application.add_handler(nieznanakomenda)
    
    # info co ile ma sie odswiezac telegram
    application.run_polling()
