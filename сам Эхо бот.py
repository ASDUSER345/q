import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Настройка логирования
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                     level=logging.INFO)

logger = logging.getLogger(__name__)

# Обработчик команды /start
def start(update, context):
    update.message.reply_text('Привет! Я бот-эхо. Напиши мне что-нибудь, и я повторю это же сообщение.')

# Обработчик сообщений
def echo(update, context):
    update.message.reply_text(update.message.text)

# Токен вашего бота
TOKEN = '7177098010:AAG13xPn3T0EeV94HEzQl9m0fOj7syXObU4'

def main():
    updater = Updater(TOKEN, use_context=True)

    dp = updater.dispatcher

    dp.add_handler(CommandHandler('start', start))
    dp.add_handler(MessageHandler(Filters.text & ~Filters.command, echo))

    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()