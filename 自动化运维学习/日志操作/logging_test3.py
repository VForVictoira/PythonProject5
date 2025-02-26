import logging

# 创建logger
logger = logging.getLogger("simple_example")
# 打印 logger 名
print(logger.name)
# 设置 logger 的日志级别
logger.setLevel(logging.INFO)

# 创建两个handler，一个负责将日志输出到终端，一个负责输出到文件
# 分别设置他们的日志级别

ch = logging.StreamHandler()
ch.setLevel(logging.DEBUG)
fh = logging.FileHandler(filename='logfile.log', encoding='utf-8', mode='w')
fh.setLevel(logging.WARNING)
# 创建一个格式化器，可以创建不同的格式化器用于不同的 handler
formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')

#设置两个handler的格式化器
ch.setFormatter(formatter)
fh.setFormatter(formatter)
#为logger添加两个handler
logger.addHandler(ch)
logger.addHandler(fh)

# 在程序中记录日志
logger.debug('debug message')
logger.info('info message')
logger.warning('warning message')
logger.error('error message')
logger.critical('critical message')
