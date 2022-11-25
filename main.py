import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='./data/ExampleBot.log',
    encoding='utf-8',
    filemode='w')

from config.settings import DADBOT_TOKEN
from src.discord_main import ExampleBot

if __name__ == '__main__':
    ExampleBot(DADBOT_TOKEN).run_example_bot()
else:
    raise SystemExit()