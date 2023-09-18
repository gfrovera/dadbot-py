import discord
from discord import app_commands
from discord.ext import commands
from dadbot import DadBot

import datetime as dt

def datetime_category() -> str:
    '''func to check what par tof the day it is'''

    now = dt.datetime.now()

    if now.time() < dt.time(12):
        return 'morning'
    elif now.time() > dt.time(17):
        return 'evening'
    else:
        return 'day'

class Greetings(commands.Cog):
    
    def __init__(self, bot: DadBot) -> None:
        self.bot: DadBot = bot

    # @commands.Cog.listener()
    # async def on_ready(self):
    #     logging.info('Bot has logged in and cog is loaded')
        
    @app_commands.command(name='hello')
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f'Hey {interaction.user.mention}! Nice to see you online',
            ephemeral=True
            )

    @app_commands.command(name='bye')
    async def bye(self, interaction: discord.Interaction):
        await interaction.response.send_message(
            f'Later {interaction.user.mention}. Have a good {datetime_category()}!',
            ephemeral=True
            )

async def setup(bot: DadBot) -> None:
    await bot.add_cog(Greetings(bot)) 
    