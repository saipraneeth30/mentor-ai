from bot.embeds.progress import get_progress_embed
from bot.views.progress_view import ProgressView


def register_progress_command(tree):

    @tree.command(
        name="progress",
        description="View your learning progress"
    )
    async def progress(interaction):

        await interaction.response.send_message(
            embed=get_progress_embed(),
            view=ProgressView(),
            ephemeral=True
        )