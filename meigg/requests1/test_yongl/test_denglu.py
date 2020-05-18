# -*- coding:utf-8 -*-
# @Time :2020/4/17 10:32
# @Email  :1084928753@qq.com
# @File :test_denglu.py
# encoding:utf-8
import unittest,json,requests,ssl
from requests1.httpjiek.httpjiek import jiek

ss=jiek()
class test_meigg(unittest.TestCase,jiek):

    def test_denfl(self):
        payload = {"username": "admin121","password":"123456"}
        data = json.dumps(payload)
        # response=ss.send_request(methon='post', data = payload)
        # print(response)


if __name__=='__main__':
    unittest.main()

