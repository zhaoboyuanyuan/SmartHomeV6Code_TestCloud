#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import unittest
from mqtt_test.public.user_uId_req_modifygasstatusoff import User_uId_req_modifygasstatusoff
from mqtt_test.mqtt_bussiness import global_value



class User_uId_req_modifygasstatusoffTestCase(unittest.TestCase):
    def setUp(self):
        self.useruIdreqmodifygasstatusoff = User_uId_req_modifygasstatusoff()

    def test_user_uId_req_modifygasstatusoff(self):
        u""""mqtt修改可燃气为布防状态"""
        self.assertEqual(self.useruIdreqmodifygasstatusoff.user_uId_req_modifygasstatusoff(),"0")

    def tearDown(self):
        self.user_uId_req_modifygasstatusoff= None

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(User_uId_req_modifygasstatusoffTestCase("test_user_uId_req_modifygasstatusoff"))
    # 这里可以添加更多的用例
    unittest.TextTestRunner().run(suite)