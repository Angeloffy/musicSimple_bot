import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
from disnake import Intents

load_dotenv()

user_storage = set()
activity = disnake.Activity(
    name="music",
    type=disnake.ActivityType.listening,
)

bot = commands.Bot(command_prefix="~!",
                   intents=Intents.all(),
                   description="play play play",
                   activity=activity,
                   )

bot.remove_command("help")


@bot.event
async def on_ready():
    print("BOT OK!")


@bot.event
async def on_voice_state_update(member: disnake.Member, before: disnake.VoiceState,
                                after: disnake.VoiceState):
    voice_client = member.guild.voice_client

    if voice_client:
        channel = voice_client.channel
        members_in_channel = channel.members

        active_users_count = sum(1 for member in members_in_channel if not member.bot)

        if active_users_count == 0:
            if voice_client.is_playing():
                voice_client.stop()
                print("Stopped playback")
        else:
            pass


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print("Load Cog: ", filename)
        bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(os.getenv("token"))
