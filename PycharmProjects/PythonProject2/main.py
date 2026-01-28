from telebot import TeleBot, types

BOTTOKEN = "8050825795:AAGh_mP2S81M0XTzr1PISIFXlVYNwN3kv0o"

bot = TeleBot(BOTTOKEN) #connection to bot

@bot.message_handler(commands=['start'])
def start(message):
    bot.send_message(message.chat.id, "привет бот запущен")


bot.infinity_polling()


