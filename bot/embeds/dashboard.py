import discord

from bot.embeds.embed_factory import create_embed


def get_dashboard_embed(
    goal: str,
    study_streak: int,
    study_hours: int,
    quiz_accuracy: int,
    current_subject: str
):

    embed = create_embed(
        title="📊 MentorAI Dashboard",
        description="Welcome to your personal learning dashboard.",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="🎯 Current Goal",
        value=goal,
        inline=False
    )

    embed.add_field(
        name="🔥 Study Streak",
        value=f"{study_streak} Days",
        inline=True
    )

    embed.add_field(
        name="⏰ Study Hours",
        value=f"{study_hours} Hours",
        inline=True
    )

    embed.add_field(
        name="📝 Quiz Accuracy",
        value=f"{quiz_accuracy}%",
        inline=False
    )

    embed.add_field(
        name="📚 Current Subject",
        value=current_subject,
        inline=False
    )

    return embed