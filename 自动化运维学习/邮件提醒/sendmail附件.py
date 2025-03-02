

import smtplib
from email._header_value_parser import Header
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = 'smtp.163.com'
mail_user = '15364071790@163.com'
mail_pass = 'RJeH2tZ2k7J9LtJL'


sender = '15364071790@163.com'
receivers= ["nordesertwolf@outlook.com","827255266@qq.com","nordesertwolf@gmail.com"]


message = MIMEMultipart()
#发件人，必须构造，可以使用 Header构造
message["From"] = sender
# 收件人列表，不是必须
message["To"] = ";".join(receivers)
# 邮件主题
message["Subject"] = 'SMTP 邮件测试'
message.attach(MIMEText('<p>这是正文:图片及附件发送测试</p><p>图片演示：</p><p><img src="cid:imagel"</p>', 'html', 'utf-8'))
# 指定图片为当前目录
fp = open('003.jpg','rb')
msgImage = MIMEImage(fp.read())
fp.close()

# 定义图片 ID，在 HTML 文本中引用
msgImage.add_header('Content-ID', '<imagel>')
message.attach(msgImage)

# 添加附件1 传送当前目录下的 test.txt 文件
att1 = MIMEText(open('test.txt','rb').read(), 'base64', 'utf-8')
att1["Content-Type"] = 'application/octet-stream'
att1["Content-Disposition"] = 'attachment; filename="test.txt"'
message.attach(att1)






try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("success!")

except smtplib.SMTPException as e:
    print(f"error: {e}")