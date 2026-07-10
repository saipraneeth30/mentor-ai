from bot.responses import get_response


def register_events(client):

    @client.event
    async def on_ready():
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