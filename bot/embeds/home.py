import discord


def get_home_embed(
    username: str,
    goal: str = "Not Set",
    level: str = "Not Set"
):
    embed = discord.Embed(
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
            "⚙ Settings\n"
            "❓ Help"
        ),
        inline=False
    )

    embed.set_footer(
        text="MentorAI • Your Personal Learning Mentor"
    )

    return embed