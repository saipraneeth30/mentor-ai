import discord


def get_help_embed():

    embed = discord.Embed(
        title="❓ MentorAI Help Center",
        description="Available MentorAI commands",
        color=discord.Color.green()
    )

    embed.add_field(
        name="/start",
        value="Start your MentorAI journey",
        inline=False
    )

    embed.add_field(
        name="/study",
        value="Open Study Center",
        inline=False
    )

    embed.add_field(
        name="/quiz",
        value="Start a quiz",
        inline=False
    )

    embed.add_field(
        name="/dashboard",
        value="View learning dashboard",
        inline=False
    )

    embed.add_field(
        name="/progress",
        value="View learning progress",
        inline=False
    )

    embed.add_field(
        name="/settings",
        value="Update your preferences",
        inline=False
    )

    embed.set_footer(
        text="MentorAI • Help"
    )

    return embed