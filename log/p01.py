import logging
import time

LOG_FORMAT = '%(asctime)s=====%(levelname)s+++++%(message)s'

logging.basicConfig(filename='myLog.log',level=logging.DEBUG,format=LOG_FORMAT)
#写法1
logging.debug('this is a debug log')
logging.info('this is a INFO log')
logging.warning('this is a WARNING log')
logging.error('this is a ERROR log')
logging.critical('this is a CRITICAL log')

#写法2
logging.log(logging.DEBUG,'THIS IS A DEBUG LOG')
logging.log(logging.INFO,'THIS IS A DEBUG INFO')
logging.log(logging.WARNING,'THIS IS A DEBUG WARNING')
logging.log(logging.ERROR,'THIS IS A DEBUG ERROR')
logging.log(logging.CRITICAL,'THIS IS A DEBUG CRITICAL')