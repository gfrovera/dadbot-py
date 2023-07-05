import asyncio
import discord
from discord import app_commands
from discord.ext import commands
from discord.ext.commands import ExtensionNotFound
from discord.ext.commands import ExtensionFailed
from discord.ext.commands import NoEntryPointError

import yaml

import logging
logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    encoding='utf-8',
    handlers=[
        logging.FileHandler('./data/ExampleBot.log',
                            mode='w'),
        logging.StreamHandler()
    ]
)

with open('./config/config.yaml', 'r') as f:
    config = yaml.safe_load(f)

# from config.settings import DADBOT_TOKEN


description = 'DadBot Slasher Command Testing'
intents = discord.Intents.default()
intents.message_content = True

init_extensions = ['cogs.greeting']

class DadBot(commands.Bot):
    def __init__(self) -> None:
        super().__init__(command_prefix='!',
                         intents=intents,
                         description=description
                         )


    async def on_ready(self) -> None:
        await self.tree.sync()
        print(f'{self.user} is synced and ready for duty!')


    async def load_cogs(self) -> None:
        for extension in init_extensions:
            try:
                await self.load_extension(extension)
            except (
                ExtensionFailed,
                ExtensionNotFound,
                NoEntryPointError,
            ):
                logging.error(f'Failed to laod cog estension: {extension}')
    

    async def start(self, debug: bool = True) -> None:
        self.debug = debug
        await self.load_cogs()
        # return await super().start(token=DADBOT_TOKEN)
        return await super().start(token=config['auth']['token'])


def run_bot() -> None:
    bot = DadBot()
    asyncio.run(bot.start())


if __name__=='__main__':
    exit()




# bot = commands.Bot(
#     command_prefix='!',
#     intents=intents,
#     description=description,
#     help_command=None
# )

# @bot.event
# async def on_ready():
#     print('DadBot reporting for duty!')
#     try:
#         synced = await bot.tree.sync()
#         print(f'DadBot is synced up {len(synced)}')
#     except Exception as e:
#         print(e)

# @bot.command()
# async def help(context):
#     await context.send('Customer Help Commands Goes Here')

# @bot.tree.command(name='hello')
# async def hello(interaction: discord.Interaction):
#     await interaction.response.send_message(f'Hey {interaction.user.mention}! Nice to see you online',
#                                             ephemeral=True)

# @bot.tree.command(name='say')
# @app_commands.describe(arg='What should I say?')
# async def say(interaction: discord.Interaction, arg: str):
#     await interaction.response.send_message(f'{interaction.user.name} said `{arg}`')


# bot.run(DADBOT_TOKEN)
