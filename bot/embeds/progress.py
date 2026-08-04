import discord

from bot.embeds.embed_factory import create_embed


def get_progress_embed(
    study_streak: int,
    study_hours: int,
    completed_topics: int,
    quiz_accuracy: int,
    goal_progress: int,
    achievement: str
):

    embed = create_embed(
        title="📈 MentorAI Progress",
        description="Track your complete learning journey.",
        color=discord.Color.gold()
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
        name="📚 Completed Topics",
        value=str(completed_topics),
        inline=True
    )

    embed.add_field(
        name="📝 Quiz Accuracy",
        value=f"{quiz_accuracy}%",
        inline=True
    )

    embed.add_field(
        name="🎯 Goal Progress",
        value=f"{goal_progress}%",
        inline=True
    )

    embed.add_field(
        name="🏆 Achievement",
        value=achievement,
        inline=False
    )

    return embed