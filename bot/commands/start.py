from discord import app_commands

from bot.embeds.welcome import create_welcome_embed
from bot.views.register_view import RegisterView


def register_start_command(tree):

    @tree.command(
        name="start",
        description="Start your MentorAI journey"
    )
    async def start(interaction):

        # Create the welcome embed
        embed = create_welcome_embed()

        # Create the Register button view
        view = RegisterView()

        # Send the embed with the button
        await interaction.response.send_message(
            embed=embed,
            view=view
        )