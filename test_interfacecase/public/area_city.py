#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

from test_interfacecase.bussiness.kernal_function import Kernal_function

class Area_city(object):
    def __init__(self):
        pass


    def area_city(self):
        read_csv = Kernal_function('area/city')
        return read_csv.api_get_answer()["resultCode"]

    def dispose(self):
        pass