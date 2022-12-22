import telebot, functions
from os import system 
system("cls")


bot = telebot.TeleBot("5852769313:AAHDojDgXsLWDbvqYcVtmJzlou9bt8wgZLM")


@bot.message_handler(commands=['wht'])
def send_welcome(message):
    bot.send_message(message.chat.id, functions.wht_valutes())
  
@bot.message_handler(content_types=['text'])
def valute(message):
    bot.send_message(message.chat.id, functions.change(message.text))


bot.polling(none_stop=True, interval=0)

