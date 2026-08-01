import discord


class DifficultySelect(discord.ui.Select):

    def __init__(self, subject: str):

        self.subject = subject

        options = [

            discord.SelectOption(
                label="Easy",
                emoji="🟢",
                description="Beginner level questions"
            ),

            discord.SelectOption(
                label="Medium",
                emoji="🟡",
                description="Intermediate level questions"
            ),

            discord.SelectOption(
                label="Hard",
                emoji="🔴",
                description="Advanced level questions"
            )

        ]

        super().__init__(
            placeholder="Choose Difficulty",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        difficulty = self.values[0]

        embed = discord.Embed(
            title="🎯 Quiz Ready",
            description=(
                f"**Subject:** {self.subject}\n"
                f"**Difficulty:** {difficulty}\n\n"
                "Click **Start Quiz** to begin."
            ),
            color=discord.Color.green()
        )

        from bot.views.quiz_question_view import QuizStartView

        await interaction.response.edit_message(
            embed=embed,
            view=QuizStartView(self.subject, difficulty)
        )


class QuizDifficultyView(discord.ui.View):

    def __init__(self, subject: str):

        super().__init__(timeout=180)

        self.add_item(DifficultySelect(subject))