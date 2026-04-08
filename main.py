import telebot

API_TOKEN = '8702965570:AAGGPb9UcroWCO_6rJZ95ykqGwUEkZigrm0'

bot = telebot.TeleBot(API_TOKEN)

if __name__ == '__main__':
    bot.polling()
