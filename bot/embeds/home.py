import discord

from bot.embeds.embed_factory import create_embed


def get_home_embed(
    username: str,
    goal: str = "Not Set",
    level: str = "Not Set"
):

    embed = create_embed(
        title="🎓 MentorAI Home",
        description=f"Welcome back, **{username}**!",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="🎯 Goal",
        value=goal,
        inline=False
    )

    embed.add_field(
        name="📚 Current Level",
        value=level,
        inline=False
    )

    embed.add_field(
        name="📌 What would you like to do?",
        value=(
            "📖 Study\n"
            "📝 Quiz\n"
            "📊 Progress\n"
            "📅 Dashboard\n"
            "⚙️ Settings\n"
            "❓ Help"
        ),
        inline=False
    )

    return embed