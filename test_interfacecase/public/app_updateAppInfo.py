#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class App_updateAppInfo(object):
    def __init__(self):
        pass

    def app_updateAppInfo(self):
        read_csv = Kernal_function('app/updateAppInfo')
        return read_csv.api_post_answer()["resultCode"]

    def dispose(self):
        pass

# user = App_updateAppInfo()
# user.app_updateAppInfo()