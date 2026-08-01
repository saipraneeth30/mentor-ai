from bot.commands.start import register_start_command
from bot.commands.study import register_study_command
from bot.commands.quiz import register_quiz_command
from bot.commands.dashboard import register_dashboard_command
from bot.commands.progress import register_progress_command
from bot.commands.settings import register_settings_command
from bot.commands.help import register_help_command
def register_commands(tree):

    register_start_command(tree)
    register_study_command(tree)
    register_quiz_command(tree)
    register_dashboard_command(tree)
    register_progress_command(tree)
    register_settings_command(tree)
    register_help_command(tree)