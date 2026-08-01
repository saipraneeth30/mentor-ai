from bot.embeds.quiz import get_quiz_embed
from bot.views.quiz_subject_view import QuizSubjectView


def register_quiz_command(tree):

    @tree.command(
        name="quiz",
        description="Start a MentorAI Quiz"
    )
    async def quiz(interaction):

        await interaction.response.send_message(
            embed=get_quiz_embed(),
            view=QuizSubjectView(),
            ephemeral=True
        )