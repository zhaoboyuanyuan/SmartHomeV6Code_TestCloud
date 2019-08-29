from test_interfacecase.common.mainFunction import mainFunction


class apiProcess(object):

    #1、获取皮肤主题列表
    def themeGetAllTheme(self):
        response = mainFunction("theme/getAllTheme").apiGetAnswer()
        return response["resultCode"]

    #2、物联公众号更改绑定的V6账号
    def userWechatUpdate(self):
        response = mainFunction("user/wechat/update").apiPostAnswer()
        return response["resultCode"]

    #3、物联公众号绑定V6账号
    def userWechatBind(self):
        response = mainFunction("user/wechat/bind").apiPostAnswer()
        return response["resultCode"]

    #4、在用户中心页面解绑三方账号
    def userThirdUnbind(self):
        response = mainFunction("user/third/unbind").apiPostAnswer()
        return response["resultCode"]

    # 5、在用户资料页面查看用户绑定的三方账号
    def userThirdGet(self):
        response=mainFunction("user/third/get").apiGetAnswer()
        return response["resultCode"]

    # 6、在用户中心页面绑定三方账号
    def userThirdBind(self):
        response=mainFunction("user/third/bind").apiPostAnswer()
        return response["resultCode"]

    # 7、三方账号绑定账号发送手机验证码
    def userThirdBindPhonecode(self):
        response=mainFunction("user/third/bind/phonecode").apiGetAnswer()
        return response["resultCode"]

    #8、保存用户意见反馈接口
    def feedbackSaveFeedback(self):
        response=mainFunction("/feedback/saveFeedback").apiPostAnswer()
        return response["resultCode"]

    #9、修改密码发送手机验证码
    def userUpdatepassPhonecode(self):
        response=mainFunction("user/updatepass/phonecode").apiGetAnswer()
        return response["resultCode"]

    #10、修改当前登录用户的头像
    def userAvatarUpdate(self):
        response=mainFunction("user/avatar/update").MEapiPostAnswer()
        return response["resultCode"]

    #11、修改当前登录用户的用户信息
    def userInfoUpdate(self):
        response=mainFunction("user/info/update").apiPostAnswer()
        return response["resultCode"]

    #12、修改密码发送手机验证码
    def userUpdatePhonePhonecode(self):
        response=mainFunction("user/update/phone/phonecode").apiGetAnswer()
        return response["resultCode"]

    #13、变更邮箱发送邮箱验证码到新邮箱和绑定新邮箱
    def userEmailUpdate(self):
        response=mainFunction("user/email/update").apiGetAnswer()
        return response["resultCode"]













# a=apiProcess()
# print(a.themeGetAllTheme())