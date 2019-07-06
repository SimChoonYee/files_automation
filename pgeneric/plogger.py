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

To put level
logging.basicConfig(filename='app.log', filemode='w', format='%(name)s - %(levelname)s - %(message)s')
logging.warning('This will get logged to a file')
'''

from pgeneric.pimport_module import *

logging.basicConfig(filename='log.log', filemode='w',
                    format='%(asctime)s %(levelname)s - %(message)s',
                    # handlers=[
                    #     logging.FileHandler("{0}.log".format('log')),
                    #     logging.StreamHandler()],
                    level=logging.DEBUG)

# https://stackoverflow.com/questions/13733552/logger-configuration-to-log-to-file-and-print-to-stdout
logging.getLogger().addHandler(logging.StreamHandler(sys.stdout))


# https://stackoverflow.com/questions/14058453/making-python-loggers-output-all-messages-to-stdout-in-addition-to-log-file