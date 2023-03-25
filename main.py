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


from dadbot import run_bot

if __name__ == '__main__':
    run_bot()
else:
    raise SystemExit()