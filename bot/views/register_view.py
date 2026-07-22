import discord

from bot.modals.registration_modal import RegistrationModal


class RegisterView(discord.ui.View):

    def __init__(self):
        super().__init__(timeout=None)

    @discord.ui.button(
        label="Register",
        style=discord.ButtonStyle.green,
        emoji="📝",
        custom_id="register_button"
    )
    async def register_button(
        self,
        interaction: discord.Interaction,
        button: discord.ui.Button
    ):
        # Open the registration form (Modal)
        await interaction.response.send_modal(
            RegistrationModal()
        )