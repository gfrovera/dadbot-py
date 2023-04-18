import discord
from discord import app_commands
from discord.ext import commands
from dadbot import DadBot


class Greetings(commands.Cog):
    
    def __init__(self, bot: DadBot) -> None:
        self.bot: DadBot = bot

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     logging.info('Bot has logged in and cog is loaded')
        
    @app_commands.command(name='hello')
    async def hello(self, interaction: discord.Interaction):
        await interaction. response.send_message(f'Hey {interaction.user.mention}! Nice to see you online',
                                                 ephemeral=True)

    @commands.command()
    async def bye(self, ctx):
        await ctx.send('later dude')

async def setup(bot: DadBot) -> None:
    await bot.add_cog(Greetings(bot))