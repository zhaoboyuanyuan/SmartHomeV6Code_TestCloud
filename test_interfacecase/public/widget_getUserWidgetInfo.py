#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Widget_getUserWidgetInfo(object):
    def __init__(self):
        pass


    def widget_getUserWidgetInfo(self):
        read_csv = Kernal_function('widget/getUserWidgetInfo')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass

