import asyncio
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

        if message.author == client.user:
            return

        print(f"{message.author}: {message.content}")

        async with message.channel.typing():

            response = await asyncio.to_thread(
                get_response,
                message.author.id,
                message.content
            )

        await message.channel.send(response.content)