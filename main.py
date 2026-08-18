from bot.discord_bot import client
from config.settings import DISCORD_TOKEN


def main():

    print("=" * 50)
    print("🚀 Starting MentorAI...")
    print("=" * 50)

    client.run(DISCORD_TOKEN)


if __name__ == "__main__":
    main()