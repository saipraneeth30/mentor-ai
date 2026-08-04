import discord

from bot.services.study_service import StudyService
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

        try:

            response = await StudyService.get_topic(
                self.subject,
                topic
            )

            study = response["study"]

            embed = discord.Embed(
                title=f"📘 {study['topic']}",
                description=study["content"],
                color=discord.Color.green()
            )

            embed.add_field(
                name="📚 Subject",
                value=study["subject"],
                inline=False
            )

            embed.add_field(
                name="🚀 Next Step",
                value="Choose a difficulty level below.",
                inline=False
            )

            embed.set_footer(
                text="MentorAI • Study Session"
            )

            await interaction.response.edit_message(
                embed=embed,
                view=DifficultyView()
            )

        except Exception as e:

            await interaction.response.edit_message(
                content=f"❌ Failed to load study material.\n\n{e}",
                embed=None,
                view=None
            )


class TopicView(discord.ui.View):

    def __init__(self, subject):

        super().__init__(timeout=180)

        self.add_item(
            TopicSelect(subject)
        )