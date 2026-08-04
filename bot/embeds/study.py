import discord

from bot.embeds.embed_factory import create_embed


def get_study_embed():

    embed = create_embed(
        title="📖 MentorAI Study Center",
        description=(
            "Welcome to your personalized learning center.\n\n"
            "Select a subject below to begin studying."
        ),
        color=discord.Color.blue()
    )

    embed.add_field(
        name="📚 Available Subjects",
        value=(
            "🌳 Data Structures\n"
            "💻 Operating Systems\n"
            "🗄 Database Management\n"
            "🌐 Computer Networks\n"
            "🤖 Machine Learning"
        ),
        inline=False
    )

    return embed