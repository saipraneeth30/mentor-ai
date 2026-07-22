import discord
from discord import app_commands

from bot.config import DISCORD_TOKEN
from bot.events import register_events
from bot.commands.start import register_start_command

# Configure intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create Discord client
client = discord.Client(intents=intents)

# Create Command Tree
tree = app_commands.CommandTree(client)

# Register Slash Commands
register_start_command(tree)

# Register all events
register_events(client, tree)

# Start the bot
client.run(DISCORD_TOKEN)