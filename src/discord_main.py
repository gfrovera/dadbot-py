import discord
from discord.ext import commands

class ExampleBot():

    def __init__(self, token):

        self.token = token    
    
        self.description = '''An example bot to showcase the discord.ext.commands extension module.
                            There are a number of utility commands being showcased here.'''
        self.intents = discord.Intents.default()
        self.intents.message_content = True

        self.examplebot = commands.Bot(description=self.description,
                                        intents=self.intents,
                                        command_prefix='$')
        self.build_example_bot()
    

    def run_example_bot(self):
        self.examplebot.run(self.token)

    def build_example_bot(self):

        @self.examplebot.event
        async def on_ready():
            print(f'We have logged in as {self.examplebot.user}')

        @self.examplebot.event
        async def on_message(message):
            if message.author == self.examplebot.user:
                return

            if message.content.startswith('$hello'):
                await message.channel.send('Hello!')


if __name__ == '__main__':
    raise SystemExit()