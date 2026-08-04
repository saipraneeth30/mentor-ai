import discord

from bot.components.navigation import NavigationView


class RefreshDashboardButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="🔄 Refresh",
            style=discord.ButtonStyle.primary
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "Dashboard refreshed successfully!",
            ephemeral=True
        )


class DashboardView(NavigationView):

    def __init__(self):

        super().__init__()

        self.add_item(RefreshDashboardButton())