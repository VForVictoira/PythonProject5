import logging
logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')

logging.basicConfig(filename='test2.log', filemode='w', level=logging.DEBUG)
