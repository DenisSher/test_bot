# Импорт комонентов
from telegram.ext import Updater
from telegram.ext import CommandHandler
from telegram.ext import MessageHandler
from telegram.ext import Filters
from settings import telegramApiUrl


# функция будет вызвана при отправке команды start
def sms(bot, update):
    print('Отправили команду /start')
    bot.message.reply_text('Приветствую, ' + format(bot.message.chat.first_name) + '!')
    print(bot.message)
    print(format(bot.message.chat.first_name))

# функция parrot() отвечает пользователю его же сообщениями
def parrot(bot, update):
    #print(bot.message.text)
    bot.message.reply_text(bot.message.text)

# Соединение с платфоромой telrgram
def main():
    my_bot = Updater(telegramApiUrl)

    my_bot.dispatcher.add_handler(CommandHandler('start', sms))
    # обработка функции повторения parrot
    my_bot.dispatcher.add_handler(MessageHandler(Filters.text, parrot))

    my_bot.start_polling()
    my_bot.idle()

main()