from pyftpdlib.authorizers import DummyAuthorizer
from pyftpdlib.handlers import FTPHandler,ThrottledDTPHandler
from pyftpdlib.servers import FTPServer
from pyftpdlib.log import LogFormatter
import logging
# 记录日志，默认情况下日志仅输出到屏幕（终端—）
# 这里既输出到屏幕又输出到文件
logger = logging.getLogger()
logger.setLevel(logging.INFO)
ch = logging.StreamHandler()
fh = logging.FileHandler(filename= 'ftp_server.log',encoding='utf-8')#默认追加到文件
ch.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
fh.setFormatter(logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s'))
logger.addHandler(ch)
logger.addHandler(fh)
# 实例化虚拟用户，这个是FTP验证首要条件
authorizer = DummyAuthorizer()
# 添加用户权限和路径，括号内的参数是（用户名、密码、用户目录、权限）
# 可以为不同用户添加不同目录和权限
authorizer.add_user('user', '123456','./',perm='elradfmw')
# 添加匿名用户，只需要路径
authorizer.add_anonymous('./')
# 初始化 FTP 句柄
handler = FTPHandler
handler.authorizer = authorizer
# 添加端口被动范围
handler.passive_ports = range(2000,2333)
# 下载上传速度限制
dtp_handler = ThrottledDTPHandler
dtp_handler.read_limit = 300 * 1024 # 300kb/s
dtp_handler.write_limit = 300 * 1024 # 300kb/s
handler.dtp_handler = dtp_handler
# 监听 IP 和端口
server = FTPServer(('0.0.0.0',21), handler)
# 最大连接数
server.max_cons = 100
server.max_cons_per_ip = 15
# 开始服务，自带日志打印信息
server.serve_forever()