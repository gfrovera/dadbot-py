import logging

logging.basicConfig(level=logging.DEBUG,
                    filename='./data/ExampleBot.log',
                    encoding='utf-8',
                    filemode='w')

from config.settings import DADBOT_TOKEN
from src.discord_main import ExampleBot

if __name__ == '__main__':
    ExampleBot(DADBOT_TOKEN).run_example_bot()
else:
    raise SystemExit()