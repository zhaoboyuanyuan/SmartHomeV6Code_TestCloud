# #!/bin/python
# # -*- coding: utf-8 -*-
# # Created by 顾洋溢
#
# import smtplib
# from email.mime.text import MIMEText            #MIMRText()定义邮件正文
# from email.mime.multipart import MIMEMultipart  #MIMEMulipart模块构造带附件
# from email.header import Header
# import sys
# sys.path.append('F:/python/test_interfacecase/unite')
# import unittest,doctest
# from test_interfacecase.unite import *
# import HTMLTestRunner
# import time
# import os
#
#
# #==============定义发送邮件==========
# def send_email(file_new):
#     # 发送邮箱服务器
#     smtpserver = 'smtp.163.com'
#
#     # 发送邮箱用户/密码(登录邮箱操作)
#     user = "guyangyi@163.com"
#     password = "wulian123"
#
#     # 发送邮箱
#     sender = "guyangyi@163.com"
#
#     # 接收邮箱
#     receiver = ["yangyi.gu@wuliangroup.com", "fangwen.fu@wuliangroup.com"]
#
#     # 发送主题
#     subject = '物联云接口自动化测试报告'
#
#     # 发送附件
#     sendfile = open(new_report(), "rb").read()
#
#     att = MIMEText(sendfile, "base64", "utf-8")
#     att["Content-Type"] = "application/octet-stream"
#     att["Content-Disposition"] = "attachment;filename = 'result.htm'"
#
#     msgRoot = MIMEMultipart('related')
#     msgRoot['Subject'] = subject
#     msgRoot.attach(att)
#     msgRoot['From'] = 'guyangyi@163.com'
#     msgRoot['To'] = ",".join(["yangyi.gu@wuliangroup.com", "fangwen.fu@wuliangroup.com"])
#     smtp = smtplib.SMTP()
#     smtp.connect(smtpserver)
#     smtp.login(user, password)
#     smtp.sendmail(sender, receiver, msgRoot.as_string())
#     smtp.quit()
#
#
#
#
#
#
# #======查找测试目录，找到最新生成的测试报告文件======
# def new_report(test_report):
#     lists = os.listdir(test_report)                                    #列出目录的下所有文件和文件夹保存到lists
#     lists.sort(key=lambda fn:os.path.getmtime(test_report + "\\" + fn))#按时间排序
#     file_new = os.path.join(test_report,lists[-1])                     #获取最新的文件保存到file_new
#     print(file_new)
#     return file_new
#
#
# if __name__ == "__main__":
#
#
