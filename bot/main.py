import os

import discord

from dotenv import load_dotenv

# Load .env file
load_dotenv()

TOKEN = os.getenv("DISCORD_TOKEN")

# Enable required intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create bot client
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    print("=" * 50)
    print(f"✅ MentorAI is online!")
    print(f"Logged in as: {client.user}")
    print("=" * 50)


client.run(TOKEN)