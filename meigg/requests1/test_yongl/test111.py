# -*- coding:utf-8 -*-
# @Time :2020/4/17 21:08
# @Email  :1084928753@qq.com
# @File :test111.py
from requests1.logginging.log import logger
import requests

url = "https://test-nicekuf.gzqqs.com/index.html#/login"

payload = {"account": "admin", "password": "123456"}
headers = {
    'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("GET", url, headers=headers, data=payload)
logger.info(">>>>>>---------开始发送请求接口地址{0},接口入参{1},入参类型{2}"
                    .format(url,payload,type(payload)))
logger.info("接口响应值{}".format(response))
print(response.text.encode('utf8'))
