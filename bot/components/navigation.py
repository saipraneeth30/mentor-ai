import discord


class HomeButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="🏠 Home",
            style=discord.ButtonStyle.secondary,
            row=4
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "🏠 Home navigation will be connected to the Home screen in the integration phase.",
            ephemeral=True
        )


class DashboardButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="📊 Dashboard",
            style=discord.ButtonStyle.secondary,
            row=4
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "📊 Dashboard navigation will be connected in the integration phase.",
            ephemeral=True
        )


class ProgressButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="📈 Progress",
            style=discord.ButtonStyle.secondary,
            row=4
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "📈 Progress navigation will be connected in the integration phase.",
            ephemeral=True
        )


class SettingsButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="⚙️ Settings",
            style=discord.ButtonStyle.secondary,
            row=4
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "⚙️ Settings navigation will be connected in the integration phase.",
            ephemeral=True
        )


class HelpButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="❓ Help",
            style=discord.ButtonStyle.secondary,
            row=4
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "❓ Help navigation will be connected in the integration phase.",
            ephemeral=True
        )


class NavigationView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=None)

        self.add_item(HomeButton())
        self.add_item(DashboardButton())
        self.add_item(ProgressButton())
        self.add_item(SettingsButton())
        self.add_item(HelpButton())