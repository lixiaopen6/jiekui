# -*- coding:utf-8 -*-
# @Time :2020/3/8 15:56
# @Email  :1084928753@qq.com
# @File :peizhiwenj.py
import requests,yaml,os,json
from requests1.api_api import rr_yaml
from login.log import logger
yaya=rr_yaml()
class jiek():
    '''封装发送所有http请求的类'''
    def __init__(self):
        url=yaya['url']
        self.headers = {'Content-Type': 'application/json'}
    def get(self,data):
        try:
            r = requests.get(url=self.url,params=data,headers=self.headers)
            return r.json()
        except BaseException as e:
            raise ('接口发生未知错误', e)
    def post(self,data,files):
        try:
              r=requests.psst(url=self.url,data=data,headers=self.headers,files=files)
              return r.json()
        except BaseException as e:
            raise ('接口发生未知错误',e)


    def detelet(self,data):
        try:
            r = requests.delete(url=self.url,data=data,headers=self.headers)
            return r.json()
        except BaseException as e:
            raise ('接口发生未知错误', e)
    def send_request(self,methon,name=None,data=None,files=None,headers=None):
        if headers:
            for key,value in headers.items():
                self.headers[key]=value
        if data:
            if isinstance(data,dict):
                data=json.dumps(data)#字典才转化字符串
        self.url=self.url+name #拼接每次请求的url
        methon=methon.upper()#忽略传入的大小区分
        res=''
        if methon=='get':
            res=self.get(data)
        elif methon=='post':
            res=self.post(data)
        elif methon=='detelet':
            res=self.detelet(data)
        logger.info("接口地址{0},接口入参{1}，""入参类型{2}，接口响应值{3}".
         format(self.url,data,type(data),res))
        return res


