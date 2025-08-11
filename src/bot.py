import os
import discord
import requests
from dotenv import load_dotenv
from utils import call_deepseek_api

load_dotenv()

DISCORD_TOKEN = os.getenv("DISCORD_TOKEN")
DEEPSEEK_API_KEY = os.getenv("DEEPSEEK_API_KEY")
DEEPSEEK_BASE_URL = os.getenv("DEEPSEEK_BASE_URL")
DEEPSEEK_MODEL = os.getenv("DEEPSEEK_MODEL", "deepseek-chat")

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot connecté en tant que {client.user}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith("$hello"):
        user_input = message.content[len("$hello "):]
        try:
            reply = call_deepseek_api(user_input, DEEPSEEK_API_KEY, DEEPSEEK_BASE_URL, DEEPSEEK_MODEL)
            await message.channel.send(reply)
        except Exception as e:
            await message.channel.send(f"⚠️ Erreur : {e}")

client.run(DISCORD_TOKEN)