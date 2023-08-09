import os
import disnake
from disnake.ext import commands
from dotenv import load_dotenv
from disnake import Intents, FFmpegPCMAudio

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
        elif voice_client.is_playing() and voice_client.channel == after.channel:
            pass
        elif active_users_count >= 1 and voice_client.is_connected():
            url_music = "http://stream.radioparadise.com"
            bitrate = channel.bitrate + 1000
            source = FFmpegPCMAudio(url_music, options=f'-b:a {bitrate}')
            voice_client.play(source)
            print("Resumed playback")


for filename in os.listdir('./cogs'):
    if filename.endswith('.py'):
        print("Load Cog: ", filename)
        bot.load_extension(f'cogs.{filename[:-3]}')

if __name__ == '__main__':
    bot.run(os.getenv("token"))
