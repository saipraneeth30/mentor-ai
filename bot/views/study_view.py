import discord

from bot.views.topic_view import TopicView


class SubjectSelect(discord.ui.Select):

    def __init__(self):

        options = [

            discord.SelectOption(
                label="Data Structures",
                emoji="🌳",
                description="Arrays, Trees, Graphs"
            ),

            discord.SelectOption(
                label="Operating Systems",
                emoji="💻",
                description="Processes, Threads"
            ),

            discord.SelectOption(
                label="Database Management",
                emoji="🗄",
                description="SQL, Transactions"
            ),

            discord.SelectOption(
                label="Computer Networks",
                emoji="🌐",
                description="OSI, TCP/IP"
            ),

            discord.SelectOption(
                label="Machine Learning",
                emoji="🤖",
                description="Regression, Classification"
            )

        ]

        super().__init__(
            placeholder="📚 Choose a Subject",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        subject = self.values[0]

        embed = discord.Embed(
            title=f"📖 {subject}",
            description=(
                f"You selected **{subject}**.\n\n"
                "Now choose a topic to start learning."
            ),
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="📚 Next Step",
            value="Select a topic from the dropdown below.",
            inline=False
        )

        embed.set_footer(
            text="MentorAI • Personalized Learning"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=TopicView(subject)
        )


class StudyView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=180)

        self.add_item(SubjectSelect())