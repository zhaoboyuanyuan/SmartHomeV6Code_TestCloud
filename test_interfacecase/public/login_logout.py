#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢



from  test_interfacecase.bussiness.kernal_function import Kernal_function

class Login_logout(object):
    def __init__(self):
        pass


    def login_logout(self):
        read_csv = Kernal_function('login/logout')
        return read_csv.sso_post_answer()["resultCode"]
        # return read_csv.sso_post_answer()

    def dispose(self):
        pass


# import requests
# import json
# from  bussiness import sha1
# import time
# import csv
# import urllib
# from urllib import parse,request
# from  bussiness.cloud_iot import iot_get_return
# from  bussiness.sso_post_headers import  post_generate_headers
# from  bussiness.open_csv import Read_file
# from  bussiness import get_serveraddress
#
# class Login_logout(object):
#     def __init__(self):
#         pass
#
#     def login_logout(self):
#         url = "https://testv2.wulian.cc:50090/sso/login/logout"  # 测试的接口url
#         get_return = iot_get_return.iot_get_return()
#         token = get_return["data"]['token']  # 接口数据
#         #print (token)
#         data = {
#             "token": token
#         }
#         headers = post_generate_headers(data)
#         req_url = url + '?' + parse.urlencode(data)  # 构建get请求
#         r = requests.post(url=url, json=data, headers=headers)  # 发送请求
#         answer = json.loads(r.text, encoding='utf-8')
#         # print(r.text)
#         # print(answer["resultCode"] )
#         return answer["resultCode"]  # 获取resultCode
#
#
#     def dispose(self):
#         pass


# login = Login_logout()
# login.login_logout()