#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import requests
import json
from  test_interfacecase.bussiness import sha1
from  test_interfacecase.bussiness import sso_post_headers
import time
from test_interfacecase.bussiness import global_value



def iot_get_return():
    url = "https://iot.wuliancloud.com:443/sso/login/byphone"  # 测试的接口url
    # data = {
    #     "phone": "18512530681",
    #     "phoneCountryCode": 86,
    #     "password": "e9ea90857363708afc42938a00719e76",
    #     "terminalId": "a50b0fff867a8ab8f252bb65f321e6bb"
    # }
    data = {
    "phone": "18168020465",
    "phoneCountryCode": 86,
    "password": "eab7c169c851f1462a140448a299d8a6",
    "terminalId":"a50b0fff867a8ab8f252bb65f321e6bb"
        }  # 接口数据
    # data = {
    #     "phone": "15951644332",
    #     "phoneCountryCode": 86,
    #     "password": "bc9b5718afdffe85fb13555347969ff5",
    #     "terminalId":"de3f365cf53a76f62b9624315349ab7a"
    # }  # 接口数据
    headers = sso_post_headers.post_generate_headers(data)
    r = requests.post(url=url,  json = data, headers=headers)  # 发送请求
    get_return = json.loads(r.text)
    global_value.set_get_return_value(get_return)
    return get_return


