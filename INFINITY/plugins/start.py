from .. import bot,openai_key
from telethon import events
import asyncio
import openai

openai.my_api_key = openai_key

@bot.on(events.NewMessage(incoming=True, pattern="hello"))
async def hello(event):
  await event.reply("How are you")

@bot.on(events.NewMessage(incoming=True, pattern="/start"))
async def hello(event):
  await event.reply("welcome")

@bot.on(events.NewMessage(incoming=True, pattern="python"))
async def hello(event):
  await event.reply("Is a programming language")
  
@bot.on(events.NewMessage(incoming=True, pattern="hii"))
async def hello(event):
  await event.reply("hello sir/medam,how can I help you?")