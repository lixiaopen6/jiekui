# -*- coding:utf-8 -*-
# @Time :2020/3/22 14:31
# @Email  :1084928753@qq.com
# @File :test_shouye.py
from POM.tongyong import gonggo
from selenium.webdriver.common.by import By
from ddt import ddt,data,unpack,file_data

class shouye(gonggo):
    url='https://sso.kuaidi100.com/sso/authorize.do'
    name=(By.XPATH,'//*[@id="name"]')
    pwd=(By.XPATH,'//*[@id="password"]')
    de=(By.XPATH,'//*[@id="submit"]')
    test = "15902127953"
    password = 'test123456'

    #输入账号
    def shur(self,text):
        self.dingwei(self.name).send_keys(self.text)
    #输入密码
    def shur1(self,text):
        self.dingwei(self.pwd).send_keys(self.password)
    #点击登录
    def click1(self):
        self.dingwei(self.de).click()
        self.quit()
    #登录流程
    def ddd(self,text,pwd):
        self.shur(text)
        self.shur1(pwd)
        self.click1()

if __name__ == '__main__':
    s=shouye('cc',shouye.url)

