from bot.embeds.settings import get_settings_embed
from bot.services.student_service import StudentService
from bot.views.settings_view import SettingsView


def register_settings_command(tree):

    @tree.command(
        name="settings",
        description="Manage your MentorAI preferences"
    )
    async def settings(interaction):

        try:

            response = await StudentService.get_settings()

            settings = response["settings"]

            embed = get_settings_embed(
                goal=settings["goal"],
                level=settings["level"],
                daily_study_hours=settings["daily_study_hours"],
                preferred_study_time=settings["preferred_study_time"],
                target_exam=settings["target_exam"]
            )

            await interaction.response.send_message(
                embed=embed,
                view=SettingsView(),
                ephemeral=True
            )

        except Exception as e:

            await interaction.response.send_message(
                f"❌ Failed to load settings.\n\n{str(e)}",
                ephemeral=True
            )