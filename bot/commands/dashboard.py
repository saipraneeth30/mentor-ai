from bot.embeds.dashboard import get_dashboard_embed
from bot.views.dashboard_view import DashboardView


def register_dashboard_command(tree):

    @tree.command(
        name="dashboard",
        description="View your MentorAI Dashboard"
    )
    async def dashboard(interaction):

        await interaction.response.send_message(
            embed=get_dashboard_embed(),
            view=DashboardView(),
            ephemeral=True
        )