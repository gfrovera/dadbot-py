import logging

logging.basicConfig(
    level=logging.DEBUG,
    format='%(asctime)s %(levelname)-8s %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S',
    filename='./data/ExampleBot.log',
    encoding='utf-8',
    filemode='w')

from test import run_bot

if __name__ == '__main__':
    run_bot()
else:
    raise SystemExit()