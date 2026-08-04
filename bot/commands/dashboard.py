from bot.embeds.dashboard import get_dashboard_embed
from bot.services.student_service import StudentService
from bot.views.dashboard_view import DashboardView


def register_dashboard_command(tree):

    @tree.command(
        name="dashboard",
        description="View your MentorAI Dashboard"
    )
    async def dashboard(interaction):

        try:

            response = await StudentService.get_dashboard()

            dashboard = response["dashboard"]

            embed = get_dashboard_embed(
                goal=dashboard["goal"],
                study_streak=dashboard["study_streak"],
                study_hours=dashboard["study_hours"],
                quiz_accuracy=dashboard["quiz_accuracy"],
                current_subject=dashboard["current_subject"]
            )

            await interaction.response.send_message(
                embed=embed,
                view=DashboardView(),
                ephemeral=True
            )

        except Exception as e:

            await interaction.response.send_message(
                f"❌ Failed to load dashboard.\n\n{str(e)}",
                ephemeral=True
            )