import discord

from bot.data.sample_quiz import QUIZ
from bot.views.quiz_result_view import QuizResultView


class AnswerButton(discord.ui.Button):

    def __init__(self, label, correct_answer, quiz_view):

        super().__init__(
            label=label,
            style=discord.ButtonStyle.primary
        )

        self.correct_answer = correct_answer
        self.quiz_view = quiz_view

    async def callback(self, interaction: discord.Interaction):

        if self.label == self.correct_answer:
            self.quiz_view.score += 1

        embed = discord.Embed(
            title="🏁 Quiz Finished",
            description=(
                f"Your Score: **{self.quiz_view.score}/1**"
            ),
            color=discord.Color.green()
        )

        await interaction.response.edit_message(
            embed=embed,
            view=QuizResultView(self.quiz_view.score)
        )


class QuizQuestionView(discord.ui.View):

    def __init__(self, subject):

        super().__init__(timeout=300)

        self.score = 0

        question = QUIZ[subject][0]

        for option in question["options"]:

            self.add_item(
                AnswerButton(
                    option,
                    question["answer"],
                    self
                )
            )


class StartQuizButton(discord.ui.Button):

    def __init__(self, subject, difficulty):

        super().__init__(
            label="▶ Start Quiz",
            style=discord.ButtonStyle.success
        )

        self.subject = subject
        self.difficulty = difficulty

    async def callback(self, interaction: discord.Interaction):

        question = QUIZ[self.subject][0]

        embed = discord.Embed(
            title=f"📝 {self.subject}",
            description=question["question"],
            color=discord.Color.orange()
        )

        await interaction.response.edit_message(
            embed=embed,
            view=QuizQuestionView(self.subject)
        )


class QuizStartView(discord.ui.View):

    def __init__(self, subject, difficulty):

        super().__init__(timeout=180)

        self.add_item(
            StartQuizButton(subject, difficulty)
        )