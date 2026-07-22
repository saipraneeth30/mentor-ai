from bot.responses import get_response


def register_events(client, tree):

    @client.event
    async def on_ready():

        # Sync all slash commands with Discord
        try:
            synced = await tree.sync()
            print(f"✅ Synced {len(synced)} slash command(s).")
        except Exception as e:
            print(f"❌ Failed to sync commands: {e}")

        print("=" * 50)
        print("✅ MentorAI is Online")
        print(f"Logged in as: {client.user}")
        print("=" * 50)


    @client.event
    async def on_message(message):

        # Ignore messages from the bot itself
        if message.author == client.user:
            return

        print(f"{message.author}: {message.content}")

        response = get_response(message.content)

        await message.channel.send(response)