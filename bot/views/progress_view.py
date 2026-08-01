import discord


class RefreshProgressButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="🔄 Refresh",
            style=discord.ButtonStyle.primary
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "Progress refreshed successfully!",
            ephemeral=True
        )


class DashboardButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="📊 Dashboard",
            style=discord.ButtonStyle.secondary
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "Dashboard navigation will be connected in the next sprint.",
            ephemeral=True
        )


class ProgressView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=180)

        self.add_item(RefreshProgressButton())
        self.add_item(DashboardButton())