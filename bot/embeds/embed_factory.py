import discord
from datetime import datetime


def create_embed(
    title: str,
    description: str,
    color: discord.Color = discord.Color.blurple()
) -> discord.Embed:
    """
    Creates a standard MentorAI embed.
    Every embed in the project should use this function.
    """

    embed = discord.Embed(
        title=title,
        description=description,
        color=color,
        timestamp=datetime.utcnow()
    )

    embed.set_footer(
        text="MentorAI • AI Study Companion"
    )

    return embed