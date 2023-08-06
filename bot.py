import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
from disnake import Intents

load_dotenv()

user_storage = set()
activity = disnake.Activity(
    name="information",
    type=disnake.ActivityType.watching,
)

bot = commands.Bot(command_prefix="p!",
                   intents=Intents.all(),
                   description="play play play",
                   activity=activity,
                    sync_commands_debug = True,
                   )

bot.remove_command("help")

@bot.event
async def on_ready():
    print("BOT OK!")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print("Load Cog: ", filename)
        bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(os.getenv("token_test"))
