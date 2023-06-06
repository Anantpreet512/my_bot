from telethon import TelegramClient

import logging

import time

openai_key = "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"

api_id = "25058178"
api_hash = "131929c537e9d4914c045f0e01d5cda3"
bot_token = "5950367156:AAHATwswCed1w3071jysoqqjxuMPLFL7ZSg"

bot = TelegramClient("rjbotz",api_id,api_hash).start(bot_token = bot_token)