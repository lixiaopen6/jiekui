# -*- coding:utf-8 -*-
# @Time :2020/3/11 11:27
# @Email  :1084928753@qq.com
# @File :httpjiek.py
'''封装发送所有http请求的类'''
import requests,unittest,json,yaml,os,logging
from requests1.gogofangfa.gonggo import rr_yaml
from requests1.logginging.log import logger


class httphttp(Exception):
    pass
yaya=rr_yaml()
class jiek():
    '''封装发送所有http请求的类'''
    def __init__(self):
        # self.url = yaya['qqurl']['qqsurl']
        self.url = yaya['url']
        self.headers = {'Content-Type': 'application/x-www-form-urlencoded'}

    def get(self,data):
        # logger.info(">>>>>>---------开始发送请求接口地址{0},接口入参{1},入参类型{2}"
        #             .format(self.url, data, type(data)))
        try:
            r = requests.get(url=self.url,params=data,headers=self.headers)
            r.encoding='utf-8'
            return r.json()
        except BaseException as e:
            raise ('接口发生未知错误', e)
    def post(self,data,files):
        # logger.info(">>>>>>---------开始发送请求接口地址{0},接口入参{1},入参类型{2}"
        #             .format(self.url, data, type(data)))
        try:
              r=requests.post(url=self.url,data=data,headers=ss.headers,files=files)
              r.encoding = 'utf-8'
              return r.json()
        except BaseException as e:
            raise httphttp('请求接口是发生未知错误',e)

    def detelet(self,data):
        try:
            r = requests.delete(url=self.url,data=data,headers=ss.headers)
            return r.json()
        except BaseException as e:
            raise httphttp('接口发生未知错误', e)
    def send_request(self,methon,name=None,data=None,headers=None,files=None):
        if headers:
            for key,value in headers.items():
                self.headers[key] = value
        # if data:
        #     if isinstance(data,dict):
        #         data=json.dumps(data)#字典才转化字符串
        # self.url=ss.url+name #拼接每次请求的url
        methon=methon.upper()#以大写的形式传入
        res=''
        if methon=='GET':
            res=self.get(data)
        elif methon=='POST':
            res=self.post(data,files)
        elif methon=='DETELET':
            res=self.detelet(data)
        logger.info(">>>>>>---------开始发送请求接口地址{0},接口入参{1},入参类型{2}"
                    .format(self.url,data,type(data)))
        logger.info("接口响应值{}".format(res))
        return res

ss=jiek()