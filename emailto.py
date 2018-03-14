# -*- coding: utf-8 -*

import smtplib
from email.mime.text import MIMEText
from email.header import Header
from email.mime.multipart import MIMEMultipart
import datetime
import time, os, sys,json,requests

# 第三方 SMTP 服务
mail_host="smtp.126.com"  #设置服务器
mail_user="laoqi1988_f1@126.com"   #用户名
mail_pass="chx175246"   #密码

sender = 'laoqi1988_f1@126.com'
receivers = 'chenhongqing@yy.com'  # 接收邮件，可设置为你的QQ邮箱或者其他邮箱

message = MIMEMultipart()

message['From'] = 'laoqi1988_f1@126.com'
message['To'] = 'chenhongqing@yy.com'

subject = 'API自动化测试报告'
message['Subject'] = Header(subject, 'utf-8')
TODAY = datetime.date.today()
CURRENTDAY = TODAY.strftime('%Y-%m-%d')
att = MIMEText(open('./Report.html', 'rb').read(), 'base64', 'utf-8')  # 设置附件的目录
att['content-type'] = 'application/octet-stream'
att['content-disposition'] = 'attachment;filename="%s result.html"'%CURRENTDAY  # 设置附件的名称
message.attach(att)

body = MIMEText(open('Report.html', 'rb').read(), 'html', 'utf-8')  # 设置字符编码



message.attach(body)
 

smtpObj = smtplib.SMTP()
smtpObj.connect(mail_host, 25)    # 25 为 SMTP 端口号
smtpObj.login(mail_user,mail_pass)
smtpObj.sendmail(sender, receivers, message.as_string())
print "邮件发送成功"
