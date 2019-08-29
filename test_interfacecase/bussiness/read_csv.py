#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢


import json
import csv
from  test_interfacecase.bussiness.open_csv import Read_file



class Read_csv(object):
    def __init__(self):
        pass


    def read_csv(self):
        read = Read_file('demo_cloud.csv')
        csv_dict = read.read_file()
        return csv_dict
