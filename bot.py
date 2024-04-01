# Zawsze to trzeba dodac, zeby program wiedzial co ty odpierdalasz.
import logging
from telegram import Update
from telegram.ext import filters, MessageHandler, CommandHandler, Application, ContextTypes, ApplicationBuilder

# Usuwa spam z konsoli, pokazuje podstawowe info z API telegrama

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.basicConfig(
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    level=logging.INFO
)

# tajne haslo dostepu do twojego bota, zeby telegram w ogole wiedzial jakiego bota chcesz ruszyc

API_KEY = '6991687705:AAFOkG3UbqmTSH5qOrnqyWNLMGQaaVRBWEE'

# REAKCJE (czyli jak program ma sie zachowywac w efekcie czegostam)
async def bodas(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="moja matka sie kurwi za regalami w kaufie ale udaje ze o tym nie wiem")
async def start(update: Update, context: ContextTypes.DEFAULT_TYPE):
    await context.bot.send_message(chat_id=update.effective_chat.id, text="cwelozo44200000")
async def konsolaszmeges(update: Update, context: ContextTypes.DEFAULT_TYPE):
    print(f"{update.message.chat.full_name} - {update.message.text}")


# to jest mega wazne, wszystko co sie dzieje w programie musi byc podpiete pod tego if'a

if __name__ == '__main__':
    print("Bot startuje se")
    application = ApplicationBuilder().token(API_KEY).build()
    
    # Tu opisujesz akcje (zeby program wiedzial kiedy i co ma robic)
    start_handler = CommandHandler('start', start)
    kutasowcy = MessageHandler(filters.Text("jajeczko"), bodas)
    bodas_handler = CommandHandler('chujek', bodas)
    konsola_handler = MessageHandler(filters.TEXT, konsolaszmeges)
    
    # deklaruje akcje (zeby program wiedzial czy tamto co pisales wczesniej jest dla beki czy na serio)
    application.add_handler(start_handler)
    application.add_handler(bodas_handler)
    application.add_handler(kutasowcy)
    application.add_handler(konsola_handler)
    
    # info co ile ma sie odswiezac telegram
    application.run_polling()
