import discord
from bot.views.difficulty_view import DifficultyView
TOPICS = {
    "Data Structures": [
        "Arrays",
        "Linked Lists",
        "Stacks",
        "Queues",
        "Trees"
    ],
    "Operating Systems": [
        "Processes",
        "Threads",
        "CPU Scheduling",
        "Deadlocks"
    ],
    "Database Management": [
        "SQL",
        "Normalization",
        "Transactions",
        "Indexing"
    ],
    "Computer Networks": [
        "OSI Model",
        "TCP/IP",
        "Routing",
        "Subnetting"
    ],
    "Machine Learning": [
        "Regression",
        "Classification",
        "Clustering",
        "Neural Networks"
    ]
}


class TopicSelect(discord.ui.Select):

    def __init__(self, subject):

        self.subject = subject

        options = [
            discord.SelectOption(
                label=topic,
                emoji="📘"
            )
            for topic in TOPICS[subject]
        ]

        super().__init__(
            placeholder="📘 Choose a Topic",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        topic = self.values[0]

        embed = discord.Embed(
            title=f"📘 {topic}",
            description=(
                f"**Subject:** {self.subject}\n\n"
                f"**Topic:** {topic}\n\n"
                "🚧 Teacher Agent integration will be added in a future sprint."
            ),
            color=discord.Color.green()
        )

        embed.add_field(
            name="🚀 Coming Next",
            value=(
                "• Difficulty Selection\n"
                "• AI Lesson Generation\n"
                "• Practice Questions\n"
                "• Quiz"
            ),
            inline=False
        )

        embed.set_footer(
            text="MentorAI • Study Session"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=DifficultyView()
            )


class TopicView(discord.ui.View):

    def __init__(self, subject):

        super().__init__(timeout=180)

        self.add_item(
            TopicSelect(subject)
        )