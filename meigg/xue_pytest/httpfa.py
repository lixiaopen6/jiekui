# -*- coding:utf-8 -*-
# @Time :2020/4/1 16:20
# @Email  :1084928753@qq.com
# @File :httpfa.py
import json
import requests


#
class httpfa(object):
    def __init__(self):
        self.set_url()

    def set_url(self):
        self.headers = {'Cotest-Type': 'application/json'}
        self.url = "http:/39.38.138.157:5001/api/"

    def get(self,data):
        res = requests.get(url=self.url, params=data, headers=self.headers)
        return res

    def post(self, data):
        res = requests.post(url=self.url, data=data, headers=self.headers)
        return res

    def send_request(self, name, method, data=None, headers=None, files=None):
        self.url+= name
        if data:
            data = json.dumps(data)
        method = method.upper()
        if headers:
            for key, value in headers.items():
                self.headers[key] = value
        if method == 'POST':
            res = self.post(data)
        else:
            res = self.get(data)

        self.set_url()
        res = json.loads(res)
        print(res)
        return res
