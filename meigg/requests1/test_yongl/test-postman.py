# -*- coding:utf-8 -*-
# @Time :2020/4/17 20:52
# @Email  :1084928753@qq.com
# @File :test-postman.py
import requests

from requests1.logginging.log import logger



url = "https://test-nicekuf.gzqqs.com/admin/login/token"

payload = {"username": "admin121","password":"123456"}
headers = {
  'Content-Type': 'application/x-www-form-urlencoded'
}

response = requests.request("post", url, headers=headers, data = payload)
logger.info(">>>>>>---------开始发送请求接口地址{0},接口入参{1},入参类型{2}"
                    .format(url,payload,type(payload)))
logger.info("接口响应值{}".format(response))
response.text.encode('utf8')
response.encoding=response.apparent_encoding
print('1111111111111',response.json())
