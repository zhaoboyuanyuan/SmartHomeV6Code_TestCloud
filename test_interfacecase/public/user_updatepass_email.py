#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class User_updatepass_email(object):
    def __init__(self):
        pass

    def user_updatepass_email(self):
        read_csv = Kernal_function('user/updatepass/email')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass
