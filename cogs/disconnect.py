import disnake
from disnake import FFmpegPCMAudio
from disnake.ext import commands


class disconnect_voice(commands.Cog):
    def __init__(self, bot: commands.Bot):
        self.bot = bot

    @commands.slash_command(name='disconnect', description="disconnect and not more", guild_ids=[])
    async def disconnect_voice_cmd(self, inter: disnake.CommandInteraction):
        await inter.response.defer()
        voice_channel = inter.guild.voice_client
        print(voice_channel)
        if voice_channel is not None:
            await voice_channel.disconnect(force=True)
            await inter.edit_original_message(content="Успешно!")
        else:
            await inter.edit_original_message(content="Бот не был подключен")

def setup(bot):
    bot.add_cog(disconnect_voice(bot))
