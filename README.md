# duck-dojo-bot

## About

This is the officially licensed, all rights reserved bot created for the Duck Dojo Telegram group. Please leave your shoes at the door. 

### Features

As of now, the features of Duck Dojo bot are:
* `/boop` - Cheer up your day with a photo of a dog

## Requirements

* Python 3
* virtualenv (optional for development)

## Getting Started

* Clone repository
* `cd duck-dojo-bot`
* `virtualenv .`
* `source bin/activate` - launches virtualenv just created.
* `pip install -r requirements.txt` will install needed packages.

Without virtualenv, you can simply execute the last step although may lead to issues with development later

## Usage

Best usage is with a systemd service:

```
[Unit]
Description=Powering the Duck Dojo Telegram bot
Documentation=https://github.com/garrettjj/duck-dojo-bot
Requires=network.target
After=network.target

[Service]
User=duck
RemainAfterExit=yes
Restart=always
WorkingDirectory=/data/duck-dojo-bot
PIDFile=/data/duck-dojo-bot/duck-bot.pid
ExecStart=python3 /data/duck-dojo-bot/bot.py

[Install]
WantedBy=multi-user.target
```

Can be run regularly without using `python3 bot.py` for testing.

## Credits

* Awesome starting tutorial at https://www.freecodecamp.org/news/learn-to-build-your-first-bot-in-telegram-with-python-4c99526765e4/ for explaining how Telegram bots work.
* Telegram's great documentation.