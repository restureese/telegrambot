from telegram.ext import Updater
import logging
import Algorithmia
from telegram.ext import CommandHandler, MessageHandler, Filters

#add logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)


#add telegram API
updater = Updater(token='<token>')

dispatcher = updater.dispatcher

#add Algorithmia API
client = Algorithmia.client('<token>')

algo = client.algo('nlp/Summarizer/0.1.3')

#command for bot
def start(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,text="Sugeng rawuh")

def restu(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,text="Dalem")
def posdim(bot, update):
	bot.sendMessage(chat_id=update.message.chat_id,text="Neng nggon sek ono wifine")


def summarize(bot, update):
    try:
        # Get the text the user sent
        text = update.message.text
        # Run it through the summarizer
        summary = algo.pipe(text)
        # Send back the result
        bot.sendMessage(chat_id=update.message.chat_id, 
                        text=summary.result)
    except UnicodeEncodeError:
        bot.sendMessage(chat_id=update.message.chat_id, 
                        text="Sorry, but I can't summarise your text.")


#enable '/start' command
start_handler = CommandHandler('start', start)
start_handler = CommandHandler('restu', restu)
start_handler = CommandHandler('posdim', posdim)


#summarize messager || meringkas pesan jika berisi text
summarize_handler = MessageHandler([Filters.text], summarize)

#dispatcher.add_handler(start_handler)
dispatcher.add_handler(start_handler)


updater.start_polling()

