import discord
from discord import app_commands
from discord.ext import commands
from dadbot import DadBot


class Jokes(commands.Cog):

    def __init__(self, bot: DadBot) -> None:
        self.bot: DadBot = bot

    # slash commands for jokes will go here


if __name__ == '__main__':
    SystemExit()