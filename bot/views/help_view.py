import discord


class SupportButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="📧 Contact Support",
            style=discord.ButtonStyle.primary
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "Support integration will be added later.",
            ephemeral=True
        )


class HomeButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="🏠 Home",
            style=discord.ButtonStyle.secondary
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "Home navigation will be connected soon.",
            ephemeral=True
        )


class HelpView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=180)

        self.add_item(SupportButton())
        self.add_item(HomeButton())