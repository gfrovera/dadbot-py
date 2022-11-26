import discord
from discord.ext import commands


class DadBot():

    def __init__(self, token):
        
        self.token = token
        self.description = '''Dadbot is a discord bot, that will reply with a randomly selected dad joke.
                               Built for fun, built for personal development/learning.'''
        self.intents = discord.Intents.all()


        self.dadbot = commands.Bot(description=self.description,
                                    intents=self.intents,
                                    command_prefix=('!', '?')
                                )
        self.build_dadbot()

    def run_dadbot(self):
        self.dadbot.run(self.token)

    def build_dadbot(self):

        @self.dadbot.event
        async def on_ready():
            print(f'{self.dadbot.user} has logged in.')

        @self.dadbot.event
        async def on_message(message) -> None:
            '''replies to user greeting with greeting'''

            author_name = str(message.author).split('#')[0]
            author_message = message.content
            author_channel = message.channel.name

            if message.author == self.dadbot.user:
                return

            if author_channel == 'bot-testing':
                if author_message.lower() in ['hi', 'hello', 'hello', 'yo',
                                            'hola', 'sup', 'hey']:
                    await message.channel.send(f'{author_message.capitalize()} {author_name}!!')
                    return
            await self.dadbot.process_commands(message)

            
if __name__ == '__main__':
    raise SystemExit()