import discord

from bot.modals.settings_modal import SettingsModal


class EditSettingsButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="✏️ Edit Settings",
            style=discord.ButtonStyle.primary
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_modal(
            SettingsModal()
        )


class BackHomeButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="🏠 Home",
            style=discord.ButtonStyle.secondary
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "🏠 Home navigation will be connected after we build the shared navigation component.",
            ephemeral=True
        )


class SettingsView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=180)

        self.add_item(EditSettingsButton())
        self.add_item(BackHomeButton())