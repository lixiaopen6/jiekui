# -*- coding:utf-8 -*-
# @Time :2020/3/22 14:05
# @Email  :1084928753@qq.com
# @File :tongyong.py
#页面公共方法
from  selenium import webdriver
from time import  sleep

class  gonggo(object):
    #初始化
    def __init__(self, chuanru, url):
        self.liulq(chuanru)
        self.driver.implicitly_wait(10)
        self.urlurl(url)


    #元素定位

    def dingwei(self, locator):
        el=self.driver.find_element(*locator)
        return el
    #浏览器初始化
    def liulq(self,chuanru):
        if chuanru=='ie':
            self.driver=webdriver.Ie()
        elif chuanru=='ff':
            self.driver=webdriver.Firefox()
        else:
            self.driver = webdriver.Chrome()
    #释放浏览器
    def quit(self):
        sleep(3)
        self.driver.close()

    def urlurl(self,url):
        self.driver.get(url)
        self.driver.maximize_window()






