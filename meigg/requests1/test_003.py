# -*- coding:utf-8 -*-
# @Time :2020/3/5 16:03
# @Email  :1084928753@qq.com
# @File :test_003.py
import requests
import unittest
class httplx(object):
    def __init__(self):
        self.url = 'http://39.107.96.138:3000/api/v1/'
        self.url1 = 'http://39.98.138.157:5001/api/'

    def qingqiu(self,rr,data,url):
        if  rr =='get':
            ff=requests.get(self.url,data)
        else:
            ff=requests.post(self.url,data)
        return ff.json()