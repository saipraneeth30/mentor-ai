import discord

from bot.views.quiz_difficulty_view import QuizDifficultyView


class QuizSubjectSelect(discord.ui.Select):

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
            title="📚 Choose Quiz Difficulty",
            description=(
                f"**Selected Subject:** {subject}\n\n"
                "Now choose your quiz difficulty level."
            ),
            color=discord.Color.blurple()
        )

        embed.add_field(
            name="🟢 Easy",
            value="Basic conceptual questions",
            inline=False
        )

        embed.add_field(
            name="🟡 Medium",
            value="Moderate difficulty questions",
            inline=False
        )

        embed.add_field(
            name="🔴 Hard",
            value="Advanced and challenging questions",
            inline=False
        )

        embed.set_footer(
            text="MentorAI • Quiz Module"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=QuizDifficultyView(subject)
        )


class QuizSubjectView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=180)

        self.add_item(QuizSubjectSelect())