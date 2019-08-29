#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import json
import csv
import urllib
import os


class Read_file(object):
    def __init__(self, file):
        self.file = file

    def read_file(self):
        #path = os.path.dirname(os.getcwd())    #  用例单独执行
        # path = os.getcwd()                      #ide 执行路径,cmd 执行路径
        path="D:\\code\\SmartHomeV6Code_TestCloud\\test_interfacecase"
        with open( path + "\\"+self.file, 'r',encoding="utf-8") as myFile:
            csv_rows = {}
            rows = csv.DictReader(myFile)
            for row in rows:
                key = row['key']
                csv_rows[key] = row["value"]  # 打印出列
            return csv_rows















