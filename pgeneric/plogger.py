'''
https://realpython.com/python-logging/

logging.debug('This is a debug message')
logging.info('This is an info message')
logging.warning('This is a warning message')
logging.error('This is an error message')
logging.critical('This is a critical message')

logging.basicConfig(format='%(asctime)s - %(message)s', level=logging.INFO)
logging.info('Admin logged in')

except Exception as e:
  logging.exception("Exception occurred")
'''

from pgeneric.pimport_module import *

logging.basicConfig(filename='log.log', filemode='w',
                    format='%(asctime)s - %(message)s',
                    # handlers=[
                    #     logging.FileHandler("{0}.log".format('log')),
                    #     logging.StreamHandler()],
                    level=logging.INFO)

# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))