# -*- coding: utf-8 -*-
import json

import requests

url="https://blog.csdn.net/pdstar/article/details/79383090"
header={}
header["User-Agent"]='Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.221 Safari/537.36 SE 2.X MetaSr 1.0'
r=requests.get(url=url,headers=header)
print(type(r.text))