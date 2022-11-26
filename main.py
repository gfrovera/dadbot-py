import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='./data/ExampleBot.log',
    encoding='utf-8',
    filemode='w')

from config.settings import DADBOT_TOKEN
from src.dadbot import DadBot

if __name__ == '__main__':
    DadBot(DADBOT_TOKEN).run_dadbot()
else:
    raise SystemExit()