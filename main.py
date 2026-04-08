import telebot

API_TOKEN = '8702965570:AAH2SlpHbDz6g2I44_52QoLIw9aOGqH96-c'

bot = telebot.TeleBot(API_TOKEN)

if __name__ == '__main__':
    bot.polling()
