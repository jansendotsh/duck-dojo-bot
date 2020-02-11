from vars.private import telegram_api
from telegram.ext import Updater, InlineQueryHandler, CommandHandler
import requests
import re
import random

def get_url():
    contents = requests.get('https://random.dog/woof.json').json()    
    url = contents['url']
    return url

def get_image_url():
    allowed_extension = ['jpg','jpeg','png']
    file_extension = ''
    while file_extension not in allowed_extension:
        url = get_url()
        file_extension = re.search("([^.]*)$",url).group(1).lower()
    return url

def boop(bot, update):
    url = get_image_url()
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def roll(bot, update):
    rollurl = 'https://dojo.burning.cloud/roll/' + random.randint(1,2)
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=rollurl)

def main():
    updater = Updater(telegram_api)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('boop',boop))
    dp.add_handler(CommandHandler('roll',roll))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
