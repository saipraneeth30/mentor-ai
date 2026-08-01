import discord


class SettingsModal(discord.ui.Modal, title="Update MentorAI Settings"):

    goal = discord.ui.TextInput(
        label="🎯 Goal",
        placeholder="Example: GATE CSE 2027",
        required=True,
        max_length=100
    )

    study_hours = discord.ui.TextInput(
        label="⏰ Daily Study Hours",
        placeholder="Example: 4",
        required=True,
        max_length=2
    )

    preferred_time = discord.ui.TextInput(
        label="🌙 Preferred Study Time",
        placeholder="Morning / Afternoon / Evening / Night",
        required=True,
        max_length=20
    )

    async def on_submit(self, interaction: discord.Interaction):

        await interaction.response.send_message(
            (
                "✅ Settings Updated Successfully!\n\n"
                f"🎯 Goal: {self.goal.value}\n"
                f"⏰ Study Hours: {self.study_hours.value}\n"
                f"🌙 Preferred Time: {self.preferred_time.value}"
            ),
            ephemeral=True
        )