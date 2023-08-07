import disnake
from disnake import FFmpegPCMAudio
from disnake.ext import commands
from bot import bot

class radio_voice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='music', description="music and not more", guild_ids=[])
    async def radio_voice_cmd(self, inter: disnake.CommandInteraction,
                              voice_channel: disnake.VoiceChannel = commands.Param(description="Укажите канал.")):
        await inter.response.defer()
        url_music = "http://stream.radioparadise.com"
        source = FFmpegPCMAudio(url_music)
        permision = voice_channel.permissions_for(inter.guild.me)
        if permision.connect:
            if permision.speak:
                if inter.guild.voice_client is None:
                    a = await voice_channel.connect(timeout=10, reconnect=True)
                else:
                    await inter.guild.voice_client.disconnect(force=True)
                    a = await voice_channel.connect(timeout=10, reconnect=True)
                a.play(source)
                await inter.edit_original_message(content="Успешно!")
            else:
                await inter.edit_original_message(content="Не достаточно прав на говорить!")
        else:
            await inter.edit_original_message(content="Не достаточно прав на подключение!")

def setup(bot):
    bot.add_cog(radio_voice(bot))
