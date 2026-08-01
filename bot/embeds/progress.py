import discord


def get_progress_embed():

    embed = discord.Embed(
        title="📈 MentorAI Progress",
        description="Track your complete learning journey.",
        color=discord.Color.gold()
    )

    embed.add_field(
        name="🔥 Study Streak",
        value="5 Days",
        inline=True
    )

    embed.add_field(
        name="⏰ Study Hours",
        value="24 Hours",
        inline=True
    )

    embed.add_field(
        name="📚 Completed Topics",
        value="18",
        inline=True
    )

    embed.add_field(
        name="📝 Quiz Accuracy",
        value="82%",
        inline=True
    )

    embed.add_field(
        name="🎯 Goal Progress",
        value="34%",
        inline=True
    )

    embed.add_field(
        name="🏆 Achievements",
        value="🥇 Consistent Learner",
        inline=False
    )

    embed.set_footer(
        text="MentorAI • Progress"
    )

    return embed