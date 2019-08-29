import smtplib
from email.mime.text import MIMEText            #MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart  #MIMEMulipart模块构造带附件
import os
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from test_interfacecase.interface_integration import interface_integration







def send_email():
    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'

    # 发送邮箱用户/密码(登录邮箱操作)
    user = "guchengcai@163.com"
    password = "wulian123"

    # 发送邮箱
    sender = "guchengcai@163.com"

    # 接收邮箱
    receiver = ["yongjian.zhao@wuliangroup.com"]
    # receiver.append("lei.wang@wuliangroup.com")  #王磊
    # receiver.append("yi.liu@wuliangroup.com") #刘毅
    # receiver.append("ren.zhong@wuliangroup.com")  #钟任
    # receiver.append("furong.wang@wuliangroup.com")


    # 发送主题
    subject = '物联云接口自动化测试报告'

    # 发送附件
    lists = os.listdir(os.getcwd())                                    #列出目录的下所有文件和文件夹保存到lists
    lists.sort(key=lambda fn:os.path.getmtime(os.getcwd() + "\\" + fn))#按时间排序
    file_new = os.path.join(os.getcwd(),lists[-1])                     #获取最新的文件保存到file_new


    msgRoot = MIMEMultipart()
    # 邮件正文是MIMEText:
    send_with_file = interface_integration()
    msgRoot.attach(MIMEText(send_with_file, 'plain', 'utf-8'))
    # 添加附件就是加上一个MIMEBase，从本地读取一个html邮件:
    with open(file_new, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('file', 'html', filename='wuliancloud_interfacetest.html')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='wuliancloud_interfacetest.html')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msgRoot.attach(mime)

    msgRoot['Subject'] = subject
    msgRoot['From'] = 'guchengcai@163.com'
    # msgRoot['To'] = ",".join(["furong.wang@wuliangroup.com","yongjian.zhao@wuliangroup.com"])
    msgRoot['To'] = ",".join(receiver)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

# send_email()
