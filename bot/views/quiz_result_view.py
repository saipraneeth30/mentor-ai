import discord


class RetryQuizButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="🔄 Retry",
            style=discord.ButtonStyle.primary
        )

    async def callback(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            "Use **/quiz** to start another quiz.",
            ephemeral=True
        )


class QuizResultView(discord.ui.View):

    def __init__(self, score):

        super().__init__(timeout=180)

        self.add_item(
            RetryQuizButton()
        )