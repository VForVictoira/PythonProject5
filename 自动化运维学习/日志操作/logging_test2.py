import logging

logging.basicConfig(level=logging.DEBUG,
                    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',#日志格式
                    datefmt='%a, %d %b %Y %H:%M:%S',#时间格式
                    filename='./test2.log', #指定文件位置
                    filemode='w') # 指定写入方式


logging.debug('debug message')
logging.info('info message')
logging.warning('warning message')
logging.error('error message')
logging.critical('critical message')