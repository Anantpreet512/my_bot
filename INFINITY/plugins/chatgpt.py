from telethon import events
from .. import bot
from .. import openai_key 
import asyncio
import openai

openai.api_key = openai_key

@bot.on(events.NewMessage(incoming=True,pattern= "(?i)/ask"))
async def ask(event):
  if event.sender_id == int(5259217283) :
    await event.reply("you are developer! you developed me very well")
  else:
    await event.reply("you are a user!how can I help you?")