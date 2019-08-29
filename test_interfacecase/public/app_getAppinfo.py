#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


from  test_interfacecase.bussiness.kernal_function import Kernal_function

class App_getAppInfo(object):
    def __init__(self):
        pass

    def app_getAppInfo(self):
        read_csv = Kernal_function('app/getAppInfo')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass

