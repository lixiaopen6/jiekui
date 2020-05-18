# -*- coding:utf-8 -*-
# @Time :2020/3/5 15:24
# @Email  :1084928753@qq.com
# @File :test_002.py

import requests
import unittest
import json

url='http://39.98.138.157:5001/api/'
data={ "username":"admin",
        "password":"123456"
}
headers = {'Content-Type': 'application/json'}
data=json.dumps(data)
s=requests.post(url+'login',data,headers=headers)
token=s.json()["token"]
print(s.url)
print(s)
print(s.json())

headers1={"token":token}
ss=requests.get(url+'user/list',headers=headers1)
print('第二个接口',ss.url)
print('第二个接口',ss)
print('第二个接口',ss.json())



