from test_interfacecase.common.mainFunction import mainFunction


class ssoProcess(object):
    # 1、post接口，手机号登陆
    def loginByPhone(self):
        response = mainFunction("login/byphone").ssoPostAnswer()
        return response["resultCode"]

    # 2、get接口，token换取mqtt连接信息
    def tokenMqtt(self):
        response = mainFunction("token/mqtt").ssoGetAnswer()
        return response["resultCode"]

    # 3、三方账号登录时绑定手机或邮箱，如果该手机或邮箱已绑定了同类型的三方账号，用户确认替换之前的账号时调用此接口；验证签名
    def loginThirdUpdate(self):
        response = mainFunction("login/third/update").ssoPostAnswer()
        return response["resultCode"]

    # 4、三方账号登录时绑定的手机或邮箱没有注册过账号，利用该手机或邮箱注册新的账号，验证签名
    def regBythird(self):
        response = mainFunction("reg/bythird").regBythirdAnswer()
        return response["resultCode"]

    # 5、三方账号登录时绑定手机或邮箱
    def loginThirdbind(self):
        response = mainFunction("login/third/bind").ssoPostAnswer()
        return response["resultCode"]

    # 6、通过手机号注册用户
    def regByphone(self):
        response = mainFunction("reg/byphone").ssoPostAnswer()
        return response["resultCode"]

    # 7、通过手机号或者邮箱找回密码并登陆
    def updatePassAndLogin(self):
        response = mainFunction("user/iot/v3/updatePassAndLogin").ssoPostAnswer()
        return response["resultCode"]

    # 8、通过手机号或者邮箱注册用户并登陆
    def registByEmailAndPhone(self):
        response = mainFunction("reg/iot/v3/registByEmailAndPhone").ssoPostAnswer()
        return response["resultCode"]

    # 9、第三方账号注册、登录
    def loginBythird(self):
        response = mainFunction("login/bythird").ssoPostAnswer()
        return response["resultCode"]

    # 10、邮箱+密码登录
    def loginByemail(self):
        response = mainFunction("login/byemail").ssoPostAnswer()
        return response["resultCode"]

    # 11、通过校验验证码完成用户的登录
    def loginPhoneEmailLogin(self):
        response = mainFunction("login/phone/email/login").ssoGetAnswer()
        return response["resultCode"]

    # 12、三方账号登录时绑定手机号发送验证码
    def userBindthirdPhonecode(self):
        response = mainFunction("user/bindthird/phonecode").ssoGetAnswer()
        return response["resultCode"]

    # 13、用户找回密码时，发送手机验证码
    def userUpdatepassPhonecode(self):
        response = mainFunction("user/updatepass/phonecode").ssoGetAnswer()
        return response["resultCode"]

    # 14、手机注册时发送验证码
    def regPhonecode(self):
        response = mainFunction("reg/phonecode").ssoGetAnswer()
        return response["resultCode"]

    # 15、安卓注册设备
    def terminalReg(self):
        response = mainFunction("terminal/reg_android").ssoPostAnswer()
        return response["resultCode"]

    # 16、ios注册设备
    def terminalRegIos(self):
        response = mainFunction("terminal/reg_ios").ssoPostAnswer()
        return response["resultCode"]

    # 17、注销账号接口
    def userRemoveUser(self):
        response = mainFunction("user/remove/user").ssoGetAnswer()
        return response["resultCode"]

    #18、申请邮箱注册
    def regByemailcode(self):
        response = mainFunction("reg/byemailcode").ssoPostAnswer()
        return response["resultCode"]

    #19、退出登录
    def loginLogout(self):
        response = mainFunction("login/logout").ssoPostAnswer()
        return response["resultCode"]

    #20、邮箱注册时发送验证码
    def regByemailcode1(self):
        response = mainFunction("reg/byemailcode1").ssoGetAnswer()
        return response["resultCode"]

    #21、验证码登录发送验证码
    def loginPhoneEmailSendCode(self):
        response = mainFunction("login/phone/email/sendCode").ssoGetAnswer()
        return response["resultCode"]




# s=ssoProcess()
# s.tokenMqtt()
