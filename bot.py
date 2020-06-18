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
    url = f'https://dojo.burning.cloud/roll/{random.randint(1,11)}.jpg'
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def chiweeners(bot, update):
    d20 = random.randint(1,20)
    if d20 < 5:
        d20 = random.randint(1,20)
        if d20 == 20:
            url = 'http://scuttle.nithingpole.com/rand_legend.png'
        else:
            url = f'http://scuttle.nithingpole.com/rand{random.randint(1,5)}.png'
    else:
        url = f'http://scuttle.nithingpole.com/doge{random.randint(1,44)}.png'
    chat_id = update.message.chat_id
    bot.send_photo(chat_id=chat_id, photo=url)

def lucky_hit(bot, update):
    url = "http://scuttle.nithingpole.com/RYO.txt"
    ryo_quotes = requests.get(url).content.decode().split("\n")
    random.shuffle(ryo_quotes)
    ryo_quote = random.choice(ryo_quotes)
    chat_id = update.message.chat_id
    bot.send_message(chat_id=chat_id, text=ryo_quote)

def main():
    updater = Updater(telegram_api)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('boop',boop))
    dp.add_handler(CommandHandler('roll',roll))
    dp.add_handler(CommandHandler('chiweeners',chiweeners))
    dp.add_handler(CommandHandler('lucky_hit',lucky_hit))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
