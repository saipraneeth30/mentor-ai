import discord


def create_welcome_embed():

    embed = discord.Embed(
        title="🤖 Welcome to MentorAI",
        description=(
            "Your personal AI Mentor for long-term learning.\n\n"
            "Prepare for:\n"
            "• GATE\n"
            "• Placements\n"
            "• AI / ML\n"
            "• DSA\n"
            "• Web Development\n\n"
            "Click **Register** to begin your journey!"
        ),
        color=discord.Color.blue()
    )

    embed.add_field(
        name="✨ Features",
        value=(
            "📚 AI Teaching\n"
            "🧠 Learning DNA\n"
            "📈 Progress Tracking\n"
            "🎯 Personalized Roadmaps"
        ),
        inline=False
    )

    embed.set_footer(
        text="MentorAI • Your Learning Companion"
    )

    return embed