import discord

from bot.embeds.embed_factory import create_embed


def get_settings_embed(
    goal: str,
    level: str,
    daily_study_hours: int,
    preferred_study_time: str,
    target_exam: str
):

    embed = create_embed(
        title="⚙️ MentorAI Settings",
        description="Manage your study preferences and account settings.",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🎯 Goal",
        value=goal,
        inline=False
    )

    embed.add_field(
        name="📚 Current Level",
        value=level,
        inline=True
    )

    embed.add_field(
        name="⏰ Daily Study Hours",
        value=f"{daily_study_hours} Hours",
        inline=True
    )

    embed.add_field(
        name="🌙 Preferred Study Time",
        value=preferred_study_time,
        inline=False
    )

    embed.add_field(
        name="📅 Target Exam",
        value=target_exam,
        inline=False
    )

    return embed