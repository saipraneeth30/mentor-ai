import discord
from discord import app_commands

from bot.config import DISCORD_TOKEN
from bot.events import register_events

from bot.commands.start import register_start_command
from bot.commands.study import register_study_command

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
register_study_command(tree)

# Register Events
register_events(client, tree)

# Run Bot
client.run(DISCORD_TOKEN)