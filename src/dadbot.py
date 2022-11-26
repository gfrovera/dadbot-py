import discord
from discord.ext import commands


class DadBot():

    def __init__(self, token):
        
        self.token = token
        self.description = '''Dadbot is a discord bot, that will reply with a randomly selected dad joke.
                               Built for fun, built for personal development/learning.'''
        self.intents = discord.Intents.default()
        self.intents.message_content = True

        self.dadbot = commands.Bot(description=self.description,
                                    intents=self.intents)
        self.build_dadbot()

    def run_dadbot(self):
        self.dadbot.run(self.token)

    def build_dadbot(self):

        @self.dadbot.event
        async def on_ready():
            print(f'{self.dadbot.user} has logged in.')


if __name__ == '__main__':
    raise SystemExit()