import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='./data/ExampleBot.log',
    encoding='utf-8',
    filemode='w')

import discord
from discord.ext import commands
from test import MyBot


class Greetings(commands.Cog):
    
    def __init__(self, bot: MyBot) -> None:
        self.bot: MyBot = bot

    @commands.Cog.listener()
    async def on_ready(self):
        logging.info('Bot has logged in and cog is loaded')
        


    @commands.command()
    async def bye(self, ctx):
        await ctx.send('later dude')

async def setup(bot: MyBot) -> None:
    await bot.add_cog(Greetings(bot))