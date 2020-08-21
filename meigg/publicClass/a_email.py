# -*- coding:utf-8 -*-
# @Time :2020/6/5 13:46
# @Email  :1084928753@qq.com
# @File :a_email.py
#实现对邮件的发送
import smtplib,time
#实现对邮件的构建
from email.mime.text import MIMEText
from email.header import Header
#如何实现对文本的发送,plain代表文件
message=MIMEText(_text='Python发送邮件的邮件文本....,',_subtype='plain',_charset='utf-8')
message['From']=Header('susu','utf-8')
message['To']=Header('susu1','utf-8')
message['Subject']=Header('鱼大佬，这是我发的邮件','utf-8')
smtpobj=smtplib.SMTP()
aa='smtp.qq.com'
try:
    # 链接SMTP服务
    smtpobj.connect(host=aa,port='587')
    #用户登录，发送账号，授权码
    smtpobj.login(user='1084928753@qq.com',password='tilhnawkttksibjg')
    sender='1084928753@qq.com'
    receiver=['1084928753@qq.com']
    smtpobj.sendmail(sender,receiver,message.as_string())
    print('邮件发送成功')
except smtplib.SMTPException:
    print('邮件发送失败')

