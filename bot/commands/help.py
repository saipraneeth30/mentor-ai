from bot.embeds.help import get_help_embed
from bot.views.help_view import HelpView


def register_help_command(tree):

    @tree.command(
        name="help",
        description="View MentorAI help and available commands"
    )
    async def help_command(interaction):

        await interaction.response.send_message(
            embed=get_help_embed(),
            view=HelpView(),
            ephemeral=True
        )