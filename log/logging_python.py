import logging
from shutil import copy2

def copyfile():
    copy2('test.txt','test2.txt')

try:
    copyfile()
except Exception:
    logging.basicConfig(filename='test.log', level=logging.INFO)
    logging.info('Something bad happeded earlier', exc_info=True)

