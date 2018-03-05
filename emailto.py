# -*- coding: utf-8 -*

import smtplib
from email.mime.text import MIMEText
from email.header import Header

# 第三方 SMTP 服务
mail_host="smtp.126.com"  #设置服务器
mail_user="laoqi1988_f1@126.com"   #用户名
mail_pass="chx175246"   #密码

sender = 'laoqi1988_f1@126.com'
receivers = 'chenhongqing@yy.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEText('自动化测试结果'+'\n'+'总用例数量', 'plain', 'utf-8')
message['From'] = 'laoqi1988_f1@126.com'
message['To'] = 'chenhongqing@yy.com'

subject = '自动化测试报告'
message['Subject'] = Header(subject, 'utf-8')

att1 = MIMEText('Report.html',_subtype="html",_charset='base64')
att1["Content-Type"] = 'application/octet-stream'
# 这里的filename可以任意写，写什么名字，邮件中显示什么名字
# att1["Content-Disposition"] = 'attachment; filename="Report1.html"'
message.attach(att1)
 

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print "邮件发送成功"
