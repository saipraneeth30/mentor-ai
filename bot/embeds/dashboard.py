import discord


def get_dashboard_embed():

    embed = discord.Embed(
        title="📊 MentorAI Dashboard",
        description="Welcome to your personal learning dashboard.",
        color=discord.Color.blue()
    )

    embed.add_field(
        name="🎯 Current Goal",
        value="GATE CSE 2027",
        inline=False
    )

    embed.add_field(
        name="🔥 Study Streak",
        value="5 Days",
        inline=True
    )

    embed.add_field(
        name="⏰ Study Hours",
        value="20 Hours",
        inline=True
    )

    embed.add_field(
        name="📝 Quiz Accuracy",
        value="82%",
        inline=False
    )

    embed.add_field(
        name="📚 Current Subject",
        value="Data Structures",
        inline=False
    )

    embed.set_footer(
        text="MentorAI • Dashboard"
    )

    return embed