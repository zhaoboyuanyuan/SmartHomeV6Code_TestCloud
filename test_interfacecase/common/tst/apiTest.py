import unittest

from test_interfacecase.common import msg
from test_interfacecase.common.process.apiProcess import apiProcess


class apiTest(unittest.TestCase):

    def setUp(self):
        self.response=apiProcess()

    def tearDown(self):
        self.response=None

    # 1、获取皮肤主题列表
    def testThemeGetAllTheme(self):
        self.assertEqual(self.response.themeGetAllTheme(), "0", msg.themeGetAllTheme)

    # 2、物联公众号更改绑定的V6账号
    def testUserWechatUpdate(self):
        self.assertEqual(self.response.userWechatUpdate(), "0", msg.userWechatUpdate)

    # 3、物联公众号绑定V6账号
    def testUserWechatBind(self):
        self.assertEqual(self.response.userWechatBind(), "0", msg.userWechatBind)

    # 4、在用户中心页面解绑三方账号,4和5是一对，先解绑后绑定
    def testUserThirdUnbind(self):
        self.assertEqual(self.response.userThirdUnbind(), "0", msg.userThirdUnbind)

    # 5、在用户中心页面绑定三方账号
    def testUserThirdBind(self):
        self.assertEqual(self.response.userThirdBind(),"0",msg.userThirdBind)

    # 6、在用户资料页面查看用户绑定的三方账号
    def testUserThirdGet(self):
        self.assertEqual(self.response.userThirdGet(), "0", msg.userThirdGet)

    # 7、三方账号绑定账号发送手机验证码
    def testUserThirdBindPhonecode(self):
        self.assertEqual(self.response.userThirdBindPhonecode(), "0", msg.userThirdBindPhonecode)

    # 8、保存用户意见反馈接口
    def testFeedbackSaveFeedback(self):
        self.assertEqual(self.response.feedbackSaveFeedback(),"0",msg.feedbackSaveFeedback)

    # 9、修改密码发送手机验证码
    def testUserUpdatepassPhonecode(self):
        self.assertEqual(self.response.userUpdatepassPhonecode(),"0",msg.userUpdatepassPhonecode)

    # # 10、修改当前登录用户的头像,图片上传有问题
    # def testUserAvatarUpdate(self):
    #     self.assertEqual(self.response.userAvatarUpdate(),"0",msg.userAvatarUpdate)

    # 11、修改当前登录用户的用户信息
    def testUserInfoUpdate(self):
        self.assertEqual(self.response.userInfoUpdate(),"0",msg.userInfoUpdate)

    # 12、修改密码发送手机验证码
    def testUserUpdatePhonePhonecode(self):
        self.assertEqual(self.response.userUpdatePhonePhonecode(),"0",msg.userUpdatePhonePhonecode)

    # 13、变更邮箱发送邮箱验证码到新邮箱和绑定新邮箱
    def testUserEmailUpdate(self):
        self.assertEqual(self.response.userEmailUpdate(),"0",msg.userEmailUpdate)


if __name__ == '__main__':
    unittest.main()

