from bot.embeds.settings import get_settings_embed
from bot.views.settings_view import SettingsView


def register_settings_command(tree):

    @tree.command(
        name="settings",
        description="Manage your MentorAI preferences"
    )
    async def settings(interaction):

        await interaction.response.send_message(
            embed=get_settings_embed(),
            view=SettingsView(),
            ephemeral=True
        )