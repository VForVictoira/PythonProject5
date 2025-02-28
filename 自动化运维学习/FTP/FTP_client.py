from ftplib import FTP
# 登录 FTP
ftp = FTP(host='localhost', user='user', passwd='123456')
ftp.encoding = 'utf-8'

ftp.cwd('test')
ftp.retrlines('LIST')
ftp.retrbinary('RETR test.txt', open('test.txt', 'wb').write)
ftp.storlines('STOR test.txt', open('test.txt', 'wb'))
for file in ftp.mlsd(path='test.txt'):
    print(file)
