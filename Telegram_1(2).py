import telebot
from telebot import custom_filters
import random

bot = telebot.TeleBot('1234567890:AAEXEMPLE_TOKEN_FICTICI_NO_VALID')

@bot.message_handler(commands=['medeix'])
def enviar_dades(message):
    temperatura = random.randrange(20,30)
    humitat = random.randrange(50,70)
    bot.send_message(message.chat.id, f'T={temperatura} H={humitat}')
    

bot.add_custom_filter(custom_filters.ChatFilter())
bot.polling(none_stop=True)
