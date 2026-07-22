import discord


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
        placeholder="Morning / Evening / Night",
        required=True,
        max_length=50
    )
    
    target_exam_date = discord.ui.TextInput(
            label="📅 Target Exam Date",
            placeholder="February 2027",
            required=True,
            max_length=50
        )

    async def on_submit(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            f"""
✅ Registration Successful!

🎯 Goal: {self.goal.value}

📚 Level: {self.level.value}

⏰ Study Hours: {self.study_hours.value}

🌙 Preferred Time: {self.preferred_time.value}
""",
            ephemeral=True
        )