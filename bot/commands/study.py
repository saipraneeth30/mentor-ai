from bot.embeds.study import get_study_embed
from bot.views.study_view import StudyView


def register_study_command(tree):

    @tree.command(
        name="study",
        description="Open MentorAI Study Center"
    )
    async def study(interaction):

        await interaction.response.send_message(
            embed=get_study_embed(),
            view=StudyView(),
            ephemeral=True
        )