import discord


class StartLearningButton(discord.ui.Button):

    def __init__(self):

        super().__init__(
            label="▶ Start Learning",
            style=discord.ButtonStyle.green,
            emoji="🚀"
        )

    async def callback(self, interaction: discord.Interaction):

        embed = discord.Embed(
            title="🧠 Preparing Your Lesson",
            description=(
                "⏳ Connecting to Teacher Agent...\n\n"
                "📚 Personalizing lesson...\n"
                "🎯 Loading study plan...\n"
                "🤖 AI response will appear here in the next sprint."
            ),
            color=discord.Color.gold()
        )

        embed.set_footer(
            text="MentorAI • Loading"
        )

        await interaction.response.edit_message(
            embed=embed,
            view=None
        )


class DifficultySelect(discord.ui.Select):

    def __init__(self):

        options = [

            discord.SelectOption(
                label="Beginner",
                emoji="🟢",
                description="Learn from basics"
            ),

            discord.SelectOption(
                label="Intermediate",
                emoji="🟡",
                description="Some prior knowledge"
            ),

            discord.SelectOption(
                label="Advanced",
                emoji="🔴",
                description="Challenge yourself"
            )

        ]

        super().__init__(
            placeholder="Choose Difficulty",
            min_values=1,
            max_values=1,
            options=options
        )

    async def callback(self, interaction: discord.Interaction):

        difficulty = self.values[0]

        embed = discord.Embed(
            title="✅ Study Session Ready",
            description=(
                f"**Difficulty:** {difficulty}\n\n"
                "Press **Start Learning** to begin."
            ),
            color=discord.Color.green()
        )

        await interaction.response.edit_message(
            embed=embed,
            view=StartLearningView()
        )


class StartLearningView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=180)

        self.add_item(StartLearningButton())


class DifficultyView(discord.ui.View):

    def __init__(self):

        super().__init__(timeout=180)

        self.add_item(DifficultySelect())