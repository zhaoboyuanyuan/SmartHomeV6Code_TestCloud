#!/bin/python
# -*- coding: utf-8 -*-
# Created by 顾洋溢

import hashlib

def str_encrypt(str):
    """
    使用sha1加密算法，返回str加密后的字符串
    """
    sha = hashlib.sha1(str)
    encrypts = sha.hexdigest()
    return encrypts

# a="wulian_app&{'phoneCountryCode': 86,'password':'bc9b5718afdffe85fb13555347969ff5', 'terminalId': 'a50b0fff867a8ab8f252bb65f321e6bb', 'phone':'15951644332'}&fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc&1558402551675".encode("utf8")
# s=str_encrypt(a)
# print(s)