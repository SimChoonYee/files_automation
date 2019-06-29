import logging


def log1():
    logging.basicConfig(level=logging.DEBUG)
    logging.debug('test')


log1()
