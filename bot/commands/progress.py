from bot.embeds.progress import get_progress_embed
from bot.services.student_service import StudentService
from bot.views.progress_view import ProgressView


def register_progress_command(tree):

    @tree.command(
        name="progress",
        description="View your learning progress"
    )
    async def progress(interaction):

        try:

            response = await StudentService.get_progress()

            progress = response["progress"]

            embed = get_progress_embed(
                study_streak=progress["study_streak"],
                study_hours=progress["study_hours"],
                completed_topics=progress["completed_topics"],
                quiz_accuracy=progress["quiz_accuracy"],
                goal_progress=progress["goal_progress"],
                achievement=progress["achievement"]
            )

            await interaction.response.send_message(
                embed=embed,
                view=ProgressView(),
                ephemeral=True
            )

        except Exception as e:

            await interaction.response.send_message(
                f"❌ Failed to load progress.\n\n{str(e)}",
                ephemeral=True
            )