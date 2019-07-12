#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2018/11/29 13:03
# @Author  : Yuquan
# @Site    :
# @File    : yagmail_.py
# @Software: PyCharm

''' 知识点：发送邮件
    使用库：第三方库yagmail
'''
import yagmail
# # 2.准备发送邮件的参数
# smtpserver = "smtp.163.com" # 发件服务器 # port = 25  # 端口
smtpserver = "smtp.qq.com" # 发件服务器
port = 465                   # 端口
sender = '1251523660@qq.com' # 发件人账户
# 163/qq邮箱用客户端授权码，不是密码
passwd = 'ykbpqkpfxsdxgbjg'
# 收件人和抄送人只有一个，参数写成str类型，多个写成list
receiver = ["1251523660@qq.com"]  # 收件人账户
cc = "985687042@qq.com" # 抄送人

# # 3.接下来就是写邮件的主题和正文内容
subject = "邮件主题"
contents = "正文内容"
#多个附件用list，单个附件用字符串
attachments = r'D:\documents\My_Py\webframework\report\result.html'
attachments = [r"D:\documents\My_Py\webframework\report\result.html", r"C:\Users\A\Desktop\temp.txt"]

# # 4.发送邮件
yag = yagmail.SMTP(sender,passwd,smtpserver,port)
yag.send(to=receiver,subject=subject,contents="yagmaill", cc=cc,attachments=attachments )
yag.close()