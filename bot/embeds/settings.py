
import discord


def get_settings_embed():

    embed = discord.Embed(
        title="⚙️ MentorAI Settings",
        description="Manage your study preferences and account settings.",
        color=discord.Color.blurple()
    )

    embed.add_field(
        name="🎯 Goal",
        value="GATE CSE 2027",
        inline=False
    )

    embed.add_field(
        name="📚 Current Level",
        value="Beginner",
        inline=True
    )

    embed.add_field(
        name="⏰ Daily Study Hours",
        value="4 Hours",
        inline=True
    )

    embed.add_field(
        name="🌙 Preferred Study Time",
        value="Evening",
        inline=False
    )

    embed.add_field(
        name="📅 Target Exam",
        value="February 2027",
        inline=False
    )

    embed.set_footer(
        text="MentorAI • Settings"
    )

    return embed