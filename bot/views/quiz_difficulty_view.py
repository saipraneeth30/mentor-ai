import discord

from bot.services.quiz_service import QuizService
from bot.views.quiz_question_view import QuizQuestionView


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

        try:

            response = await QuizService.start_quiz(
                self.subject,
                difficulty
            )

            quiz = response["quiz"]

            question = quiz["questions"][0]

            embed = discord.Embed(
                title="📝 Question 1",
                description=question["question"],
                color=discord.Color.orange()
            )

            embed.add_field(
                name="🅰 Option A",
                value=question["options"][0],
                inline=False
            )

            embed.add_field(
                name="🅱 Option B",
                value=question["options"][1],
                inline=False
            )

            embed.add_field(
                name="🅲 Option C",
                value=question["options"][2],
                inline=False
            )

            embed.add_field(
                name="🅳 Option D",
                value=question["options"][3],
                inline=False
            )

            embed.set_footer(
                text=f"{quiz['subject']} • {quiz['difficulty']}"
            )

            await interaction.response.edit_message(
                embed=embed,
                view=QuizQuestionView(
                    quiz["questions"]
                    )
            )

        except Exception as e:

            await interaction.response.edit_message(
                content=f"❌ Failed to load quiz.\n\n{e}",
                embed=None,
                view=None
            )


class QuizDifficultyView(discord.ui.View):

    def __init__(self, subject: str):

        super().__init__(timeout=180)

        self.add_item(
            DifficultySelect(subject)
        )