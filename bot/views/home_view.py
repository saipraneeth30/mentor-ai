import discord


class HomeView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Study",
        emoji="📖",
        style=discord.ButtonStyle.primary
    )
    async def study(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "📖 Study module coming soon!",
            ephemeral=True
        )

    @discord.ui.button(
        label="Quiz",
        emoji="📝",
        style=discord.ButtonStyle.success
    )
    async def quiz(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "📝 Quiz module coming soon!",
            ephemeral=True
        )

    @discord.ui.button(
        label="Progress",
        emoji="📊",
        style=discord.ButtonStyle.secondary
    )
    async def progress(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "📊 Progress module coming soon!",
            ephemeral=True
        )

    @discord.ui.button(
        label="Dashboard",
        emoji="📅",
        style=discord.ButtonStyle.secondary,
        row=1
    )
    async def dashboard(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "📅 Dashboard coming soon!",
            ephemeral=True
        )

    @discord.ui.button(
        label="Settings",
        emoji="⚙",
        style=discord.ButtonStyle.secondary,
        row=1
    )
    async def settings(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "⚙ Settings coming soon!",
            ephemeral=True
        )

    @discord.ui.button(
        label="Help",
        emoji="❓",
        style=discord.ButtonStyle.secondary,
        row=1
    )
    async def help(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        await interaction.response.send_message(
            "❓ Help coming soon!",
            ephemeral=True
        )