

import smtplib
from email._header_value_parser import Header
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# 第三方 SMTP 服务
mail_host = 'smtp.163.com'
mail_user = '15364071790@163.com'
mail_pass = 'RJeH2tZ2k7J9LtJL'


sender = '15364071790@163.com'
receivers= ["nordesertwolf@outlook.com","827255266@qq.com","nordesertwolf@gmail.com"]

# 构造正文
message = MIMEText('测试','plain','utf-8')
#发件人，必须构造，可以使用 Header构造
message["From"] = sender
# 收件人列表，不是必须
message["To"] = ";".join(receivers)
# 邮件主题
message["Subject"] = 'SMTP 邮件测试'

try:
    smtpObj = smtplib.SMTP()
    smtpObj.connect(mail_host, 25)
    smtpObj.login(mail_user, mail_pass)
    smtpObj.sendmail(sender, receivers, message.as_string())
    print("success!")

except smtplib.SMTPException as e:
    print(f"error: {e}")