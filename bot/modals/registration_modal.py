import discord

from bot.services.student_service import StudentService
from bot.embeds.home import get_home_embed
from bot.views.home_view import HomeView


class RegistrationModal(discord.ui.Modal, title="MentorAI Student Registration"):

    goal = discord.ui.TextInput(
        label="🎯 What is your goal?",
        placeholder="Example: GATE CSE 2027",
        required=True,
        max_length=100
    )

    level = discord.ui.TextInput(
        label="📚 Current Level",
        placeholder="Beginner / Intermediate / Advanced",
        required=True,
        max_length=50
    )

    study_hours = discord.ui.TextInput(
        label="⏰ Daily Study Hours",
        placeholder="Example: 4",
        required=True,
        max_length=10
    )

    preferred_time = discord.ui.TextInput(
        label="🌙 Preferred Study Time",
        placeholder="Morning / Afternoon / Evening / Night",
        required=True,
        max_length=50
    )

    target_exam_date = discord.ui.TextInput(
        label="📅 Target Exam Date",
        placeholder="Example: February 2027",
        required=True,
        max_length=50
    )

    async def on_submit(self, interaction: discord.Interaction):

        try:
            student_data = {
                "goal": self.goal.value,
                "level": self.level.value,
                "study_hours": int(self.study_hours.value),
                "preferred_time": self.preferred_time.value,
                "target_exam_date": self.target_exam_date.value,
            }

            response = await StudentService.register_student(student_data)

            embed = get_home_embed(
                username=interaction.user.display_name,
                goal=response["student"]["goal"],
                level=response["student"]["level"]
            )

            await interaction.response.send_message(
                embed=embed,
                view=HomeView(),
                ephemeral=True
            )

        except ValueError:
            await interaction.response.send_message(
                "❌ Study Hours must be a valid number.",
                ephemeral=True
            )

        except Exception as e:
            await interaction.response.send_message(
                f"❌ Registration Failed!\n\n{str(e)}",
                ephemeral=True
            )
            