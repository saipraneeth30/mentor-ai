import discord


def get_quiz_embed():

    embed = discord.Embed(
        title="📝 MentorAI Quiz Center",
        description=(
            "Test your knowledge with personalized quizzes.\n\n"
            "📚 Select a subject below to begin."
        ),
        color=discord.Color.orange()
    )

    embed.add_field(
        name="📖 Available Subjects",
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
        text="MentorAI • Quiz Module"
    )

    return embed