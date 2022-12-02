import asyncio
import discord
from discord.ext import commands
from discord.ext.commands import ExtensionNotFound, ExtensionFailed, NoEntryPointError

from config.settings import DADBOT_TOKEN

description = 'structure and cog testing'
intents = discord.Intents.default()
intents.message_content = True

init_extensions = ['cogs.greeting']

# bot = commands.Bot(intents=intents, command_prefix='!')

class MyBot(commands.Bot):

    def __init__(self) -> None:
        super().__init__(command_prefix='!',intents=intents, description=description)

    async def on_ready(self) -> None:
        await self.tree.sync()
        print(f'Bot is ready -> {self.user}')


    async def load_cogs(self) -> None:
        for extension in init_extensions:
            try:
                await self.load_extension(extension)
            except (
                ExtensionFailed,
                ExtensionNotFound,
                NoEntryPointError,
            ):
                print(f'Failed to load cog extension {extension}')

    async def start(self, debug: bool = False) -> None:
        self.debug = debug
        await self.load_cogs()
        return await super().start(token=DADBOT_TOKEN)

def run_bot() -> None:
    bot = MyBot()
    asyncio.run(bot.start())

if __name__ == '__main__':
    exit()

# @bot.command()
# async def hello(ctx):
#     await ctx.send('Oh hey there')

# async def main():
#     await bot.load_extension('cogs.greeting')
#     await bot.start(token = DADBOT_TOKEN)

# asyncio.run(main())


