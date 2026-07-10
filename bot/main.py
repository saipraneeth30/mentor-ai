import discord

from bot.config import DISCORD_TOKEN
from bot.events import register_events

# Configure intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create Discord client
client = discord.Client(intents=intents)

# Register all events
register_events(client)

# Start the bot
client.run(DISCORD_TOKEN)