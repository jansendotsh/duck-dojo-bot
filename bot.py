from telegram.ext import Updater, CommandHandler
import logging
import os
import random
import requests

def roll(update, context):
    url = f'https://dojo.burning.cloud/roll/{random.randint(1,11)}.jpg'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def chiweeners(update, context):
    d20 = random.randint(1,20)
    if d20 < 5:
        d20 = random.randint(1,20)
        if d20 == 20:
            url = 'http://scuttle.nithingpole.com/rand_legend.png'
        else:
            url = f'http://scuttle.nithingpole.com/rand{random.randint(1,5)}.png'
    else:
        url = f'http://scuttle.nithingpole.com/doge{random.randint(1,44)}.png'
    context.bot.send_photo(chat_id=update.effective_chat.id, photo=url)

def lucky_hit(update, context):
    url = "http://scuttle.nithingpole.com/RYO.txt"
    ryo_quotes = requests.get(url).content.decode().split("\n")
    random.shuffle(ryo_quotes)
    ryo_quote = random.choice(ryo_quotes)
    context.bot.send_message(chat_id=update.effective_chat.id, text=ryo_quote)

def main():
    telegram_api = os.environ['TELEGRAM_TOKEN']
    updater = Updater(token=telegram_api, use_context=True)
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',level=logging.INFO)
    dp = updater.dispatcher
    dp.add_handler(CommandHandler('roll',roll))
    dp.add_handler(CommandHandler('chiweeners',chiweeners))
    dp.add_handler(CommandHandler('lucky_hit',lucky_hit))
    updater.start_polling()
    updater.idle()

if __name__ == '__main__':
    main()
