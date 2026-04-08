import telebot

API_TOKEN = 'YOUR_API_TOKEN'

bot = telebot.TeleBot(API_TOKEN)

if __name__ == '__main__':
    bot.polling()