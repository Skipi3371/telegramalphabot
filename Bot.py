from importlib.resources import contents
import telebot  
token = '5103697994:AAEkl4RM1Juj-kV0Hs-fI0sDOe9GWuYXcFE'
bot - telebot.Telebot(token)

@bot.message_handler(commands=['start'])

def start(message):
    bot.forward_message(chat_id='-1001708938282', from_chat_id='-1001571508006', message_id=message.id)

bot.polling()