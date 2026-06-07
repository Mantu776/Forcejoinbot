import telebot

TOKEN = 8987730677:AAEUPxbms-z7IzuQrQ6XF7lkPcrB7SI6tbE

bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start'])
def start(message):
    bot.reply_to(message, "Hello! Force Join Bot Working ✅")

print("Bot Started...")
bot.infinity_polling()
