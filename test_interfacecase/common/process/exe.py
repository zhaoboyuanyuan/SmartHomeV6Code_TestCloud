# -*- coding: utf-8 -*-
import json
from collections import OrderedDict
from urllib import parse

import requests
import time

from test_interfacecase.bussiness import sha1

# 关于签名
#        每个app会分配一个partnerId和partnerKey
#        签名规则：
#               partnerId+"&"+参数部分+"&"+partnerKey+"&"+当前时间戳(毫秒)
#               上述字符串进行sha1加密然后转换成小写字符串,就是本次请求的签名
#        对于GET请求
#               参数部分为：所有参数按照参数名升序排序，通过"&"拼接起来
#        对于POST请求
#               参数部分为：request的body

from test_interfacecase.common.process import location
from test_interfacecase.common.readFile import readFile

address = location.address()["OfficialServerAddress"]

# token换取mqtt连接信息接口，get请求
inf1 = {"url": "sso/token/mqtt", "method": "get",
        "data": {
            "token": "token",
        }
        }
#三方账号登录时绑定手机或邮箱，如果该手机或邮箱已绑定了同类型的三方账号，用户确认替换之前的账号时调用此接口；
inf2 = {"url": "sso/login/third/update", "method": "post",
        "data": {
            "thirdType": 3,
            "terminalId": "f4cede55dfdcf29ab56c2adbf0ee4145",
            "openId": "1820499241",
            "phone": "18066111626",
            "phoneCountryCode": "86",
            "email": "***",
            "authCode": "123456"
        }
        }

class function(object):
    def __init__(self,key):
        self.key=key
        self.dict = readFile("demo_cloud.csv").readfile()


    # 复杂的操作，header,拼接字符串，get与post的请求的签名
    def header(self,index,inf):
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        # 当前时间戳(毫秒)
        t = time.time()
        now = str(int(round(t * 1000)))

        if index == 0:
            # get参数，将各个接口中的参数按照名升序排序，通过"&"拼接起来
            getParam = inf["data"]
            getParam = sorted(getParam.items(), key=lambda item: item[0])  # 升序排序
            getParam = parse.urlencode(getParam, encoding="utf-8")  # 通过"&"拼接起来
            getParam = parse.unquote(getParam,encoding="utf-8")
            sign = partnerId + "&" + getParam + "&" + partnerkey + "&" + now
            # print ("sign:"+sign)

        elif index == 1:
            # post参数，request的body就是各个接口中的参数
            postParam = json.dumps(inf["data"])  # 把字典转换为字符串
            sign = partnerId + "&" + postParam + "&" + partnerkey + "&" + now

        sign = sign.encode("utf-8")
        sign1 = sha1.str_encrypt(sign).lower()
        header = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": now, "WL-SIGN": sign1,
                  "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb"}
        return header

    def apiHeader(self,index,inf,token):
        partnerId = "wulian_app"
        partnerkey = "fb1bbde01c9a4d45d82d5f5107b1f4dd7c105af06c928ce14878cdda03874dcc"
        # 当前时间戳(毫秒)
        t = time.time()
        now = str(int(round(t * 1000)))

        if index == 0:
            # get参数，将各个接口中的参数按照名升序排序，通过"&"拼接起来
            getParam = inf["data"]
            getParam = sorted(getParam.items(), key=lambda item: item[0])  # 升序排序
            getParam = parse.urlencode(getParam, encoding="utf-8")  # 通过"&"拼接起来
            getParam = parse.unquote(getParam,encoding="utf-8")
            sign = partnerId + "&" + getParam + "&" + partnerkey + "&" + now
            # print ("sign:"+sign)

        elif index == 1:
            # post参数，request的body就是各个接口中的参数
            postParam = json.dumps(inf["data"])  # 把字典转换为字符串
            sign = partnerId + "&" + postParam + "&" + partnerkey + "&" + now

        sign = sign.encode("utf-8")
        sign1 = sha1.str_encrypt(sign).lower()
        header = {"Content-Type": "application/json", "WL-PARTNER-ID": "wulian_app", "WL-TIMESTAMP": now, "WL-SIGN": sign1,
                  "WL-TID": "a50b0fff867a8ab8f252bb65f321e6bb","WL-TOKEN":token}
        return header


    # 账号密码登录，获取连接dict,包涵token信息
    def connect(self):
        # 通过手机号+密码登录，post请求
        account = {"url": "sso/login/byphone", "data": {
            "phone": "15951644332",
            "phoneCountryCode": 86,
            "password": "bc9b5718afdffe85fb13555347969ff5",
            "terminalId": "a50b0fff867a8ab8f252bb65f321e6bb"
        }
                   }
        url = address + account["url"]
        data = account["data"]
        r = requests.post(url=url, json=data, headers=self.header(1, account))
        # print(r.text)
        return json.loads(r.text, encoding="utf-8")


    # get请求
    def get(self):
        inf=json.loads(self.dict[self.key],encoding="utf-8")
        token = self.connect()["data"]["token"]
        uId= self.connect()["data"]["uId"]
        if "token" in inf["data"]:
            inf["data"]["token"] = token
        if "uId" in inf["data"]:
            inf["data"]["uId"] = uId
        url = parse.urlencode(inf["data"], encoding="utf-8")
        url = parse.unquote(url,encoding="utf-8")
        url = address + inf["url"]+"?"+url
        r = requests.get(url=url, headers=self.header(0, inf))
        print (r.url)
        return json.loads(r.text,encoding="utf-8")

    # get请求
    def apiGet(self):
        inf=json.loads(self.dict[self.key],encoding="utf-8")
        token = self.connect()["data"]["token"]
        uId= self.connect()["data"]["uId"]
        if "token" in inf["data"]:
            inf["data"]["token"] = token
        if "uId" in inf["data"]:
            inf["data"]["uId"] = uId
        url = parse.urlencode(inf["data"], encoding="utf-8")
        url = parse.unquote(url,encoding="utf-8")
        url = address + inf["url"]+"?"+url
        head=self.apiHeader(0, inf,self.connect()["data"]["token"])
        r = requests.get(url=url, headers=head)
        return json.loads(r.text,encoding="utf-8")


    # post请求
    def post(self):
        inf=json.loads(self.dict[self.key],encoding="utf-8")
        token = self.connect()["data"]["token"]
        uId = self.connect()["data"]["uId"]
        if "token" in inf["data"]:
            inf["data"]["token"] = token
        if "uId" in inf["data"]:
            inf["data"]["uId"] = uId
        url = address + inf["url"]
        data = inf["data"]
        r = requests.post(url=url, json=data, headers=self.header(1, inf))
        return json.loads(r.text, encoding="utf-8")

    # post请求
    def apiPost(self):
        inf=json.loads(self.dict[self.key],encoding="utf-8")
        token = self.connect()["data"]["token"]
        uId = self.connect()["data"]["uId"]
        if "token" in inf["data"]:
            inf["data"]["token"] = token
        if "uId" in inf["data"]:
            inf["data"]["uId"] = uId
        url = address + inf["url"]
        data = inf["data"]
        r = requests.post(url=url, json=data, headers=self.apiHeader(1, inf,self.connect()["data"]["token"]))
        return json.loads(r.text, encoding="utf-8")



f=function("user/wechat/update")
print(f.apiPost())

# 1、address处理   ok
# 2、集合unitest框架 ok
# 3、集合接口  ok
# 4、处理sso与其他接口的差异
# 5、post与get的处理    ok

