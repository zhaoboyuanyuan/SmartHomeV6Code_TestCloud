import smtplib
from email.mime.text import MIMEText            #MIMRText()定义邮件正文
from email.mime.multipart import MIMEMultipart  #MIMEMulipart模块构造带附件
import os
from email import encoders
from email.header import Header
from email.mime.base import MIMEBase
from test_interfacecase.interface_integration import interface_integration

def send_email():
    #邮件发送内容
    text = '''物联云接口测试条目如下:
                SSO接口：
                1、SSO接口-token换取mqtt连接信息
                2、SSO接口-【登录】三方账号登录时替换已绑定的同类型账号
                3、SSO接口-【登录】三方账号登录时用手机或邮箱注册新账号
                4、SSO接口-【登录】三方账号登录时绑定手机或邮箱
                5、SSO接口-【登录】手机号+密码登录
                6、SSO接口-【登录】手机或邮箱修改密码并登陆
                7、SSO接口-【登录】第三方登录
                8、SSO接口-【登录】邮箱+密码登录
                9、SSO接口-【登录】验证码登录
                10、SSO接口-三方账号登录时绑定手机号发送验证码
                11、SSO接口-修改密码发送手机验证码
                12、SSO接口-修改密码发送邮箱验证码
                13、SSO接口-手机注册发送验证码
                14、SSO接口-找回密码时检查手机或者邮箱验证码
                15、SSO接口-注册时检查手机或者邮箱验证码
                16、SSO接口-注册设备
                17、SSO接口-申请邮箱注册
                18、SSO接口-退出登录
                19、SSO接口-邮箱注册发送验证码
                20、SSO接口-验证码登录发送验证码
                API接口:
                21、API接口-app换肤接口(获取皮肤主题列表)
                22、API接口-查询widget信息
                23、API接口-三方账号-查询已绑定的三方账号
                24、API接口-三方账号-绑定三方账号
                25、API接口-三方账号绑定手机用户发送手机验证码
                26、API接口-三方账号-解绑三方账号
                27、API接口-保存用户意见反馈
                28、API接口-修改密码发送手机验证码
                29、API接口-通过原密码修改密码
                30、API接口-修改当前登录用户的用户信息
                31、API接口-修改手机号发送手机验证码
                32、API接口-发送修改绑定邮箱的邮件到新邮箱,也是绑定邮箱的接口
                33、API接口-发送修改绑定邮箱的邮件到旧邮箱
                34、API接口-变更手机号
                35、API接口-变更手机号发送手机验证码
                36、API接口-变更手机号发送手机验证码到旧手机
                37、API接口-变更手机号校验旧手机的验证码
                38、API接口-变更邮箱校验新邮箱的验证码,也是验证绑定邮箱的接口
                39、API接口-变更邮箱校验旧邮箱的验证码
                40、API接口-手机号+验证码修改用户密码
                41、API接口-申请修改用户密码邮件(通过邮箱修改密码)
                42、API接口-积分-用户签到
                43、API接口-积分-获取当前用户的积分信息
                44、API接口-积分-获取当前用户的积分增加与消费记录
                45、API接口-积分-获取当前用户的签到信息
                46、API接口-获取当前登录用户的用户信息
                47、API接口-【广告页】- 查询 中文
                48、API接口-【广告页】- 查询 英文
                50、物联公众号绑定V6账号发送验证码
                51、物联公众号绑定V6账号
                52、物联公众号更改绑定的V6账号
                53、查询省份
                54、获取banner列表
                接口
                55、app分册
                56、APP检查更新的接口
                UAS接口
                57、UAS接口-保存设备键值对信息
                58、UAS接口-查询设备键值对信息
                59、UAS接口-推送
                60、UAS接口-查询Bc锁下的摄像机Id
                61、UAS接口-获取爱看OSS子账号数据
                62、UAS接口-获取sip信息
                63、UAS接口-删除用户消息中心报警消息
                64、UAS接口-取消设备分享
                65、UAS接口-查询用户下绑定的设备信息
                66、UAS接口-查询用户下绑定的设备详细信息
                67、UAS接口-查询设备统计数据
                68、UAS接口-校验设备是否绑定
                69、UAS接口-检验设备是否是v6支持
                70、UAS接口-获取分享出去的子设备列表
                71、UAS接口-获取或清零用户网关下子设备告警未读数
                72、UAS接口-获取用户下的设备列表包括绑定的设备和分享的设备
                73、UAS接口-顶级设备下的子设备信息
                74、UAS接口-获取绑定关系码
                75、UAS接口-获取设备绑定的用户和已分享的用户
                76、UAS接口-获取设备静态信息
                77、UAS接口-记录用户当前选中的网关并校验密码
                78、UAS接口-设备分享
                79、用户推送信息相关接口
                80、设备历史数据相关接口
                81、保存设备间关系
                82、查询设备间关系
                83、删除设备间关系
                84、查询城市
                85、查询城市的天气温湿度接口
                86、ent接口-向往音箱
             '''

    # 发送邮箱服务器
    smtpserver = 'smtp.163.com'

    # 发送邮箱用户/密码(登录邮箱操作)
    # user = "guchengcai@163.com"
    # password = "wulian123"

    user = "15951644332@163.com"
    password = "zhaoboyuan54321"


    # 发送邮箱
    sender = user

    # 接收邮箱
    receiver = ["1309817607@qq.com"]
    # receiver.append("lei.wang@wuliangroup.com")  #王磊
    # receiver.append("yi.liu@wuliangroup.com") #刘毅
    # receiver.append("ren.zhong@wuliangroup.com")  #钟任
    # receiver.append("furong.wang@wuliangroup.com")


    # 发送主题
    subject = '物联云接口自动化测试报告'

    # # 发送附件
    # lists = os.listdir(os.getcwd())                                    #列出目录的下所有文件和文件夹保存到lists
    # lists.sort(key=lambda fn:os.path.getmtime(os.getcwd() + "\\" + fn))#按时间排序
    # file_new = os.path.join(os.getcwd(),lists[-1])                     #获取最新的文件保存到file_new

    file_new="D:\\code\\SmartHomeV6Code_TestCloud\\result.html"


    msgRoot = MIMEMultipart()
    # 邮件正文是MIMEText:
    send_with_file = text
    msgRoot.attach(MIMEText(send_with_file, 'plain', 'utf-8'))
    # 添加附件就是加上一个MIMEBase，从本地读取一个html邮件:
    with open(file_new, 'rb') as f:
        # 设置附件的MIME和文件名，这里是png类型:
        mime = MIMEBase('file', 'html', filename='result.html')
        # 加上必要的头信息:
        mime.add_header('Content-Disposition', 'attachment', filename='result.html')
        mime.add_header('Content-ID', '<0>')
        mime.add_header('X-Attachment-Id', '0')
        # 把附件的内容读进来:
        mime.set_payload(f.read())
        # 用Base64编码:
        encoders.encode_base64(mime)
        # 添加到MIMEMultipart:
        msgRoot.attach(mime)

    msgRoot['Subject'] = subject
    msgRoot['From'] = user
    # msgRoot['To'] = ",".join(["furong.wang@wuliangroup.com","yongjian.zhao@wuliangroup.com"])
    msgRoot['To'] = ",".join(receiver)
    smtp = smtplib.SMTP()
    smtp.connect(smtpserver)
    smtp.login(user, password)
    smtp.sendmail(sender, receiver, msgRoot.as_string())
    smtp.quit()

send_email()
