import discord


def get_study_embed():

    embed = discord.Embed(
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

    embed.set_footer(
        text="MentorAI • Learn one step at a time"
    )

    return embed