import discord
from discord import app_commands

from bot.config import DISCORD_TOKEN
from bot.events import register_events

from bot.commands import register_commands
# Configure intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

# Create Discord client
client = discord.Client(intents=intents)

# Create Command Tree
tree = app_commands.CommandTree(client)

# Register Slash Commands
register_commands(tree)
# Register Events
register_events(client, tree)

# Run Bot
client.run(DISCORD_TOKEN)