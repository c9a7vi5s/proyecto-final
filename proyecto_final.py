import os
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = os.getenv("DISCORD_TOKEN")

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f"Bot conectado como: {client.user}")

@client.event
async def on_message(message):

    if message.author == client.user:
        return

    if message.content.lower() == "!hola":
        await message.channel.send(f"Hola, {message.author.display_name}!")

    if message.content.lower() == "!ping":
        await message.channel.send("Pong! 🏓")

client.run(TOKEN)
