import telebot
from telebot import custom_filters
import random

TOKEN = '1234567890:AAEXEMPLE_TOKEN_FICTICI_NO_VALID'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['medeix'])
def enviar_dades(message):
    temperatura = random.randrange(20, 30)
    humitat = random.randrange(50, 70)
    bot.send_message(message.chat.id, f'T={temperatura} H={humitat}')

try:
    bot.add_custom_filter(custom_filters.ChatFilter())
    bot.polling(none_stop=True)

except KeyboardInterrupt:
    print("Aturant el bot...")
    bot.stop_polling()
    print("Programa finalitzat")
