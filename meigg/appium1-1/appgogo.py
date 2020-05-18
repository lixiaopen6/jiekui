# -*- coding:utf-8 -*-
# @Time :2020/2/24 17:16
# @Email  :1084928753@qq.com
# @File :appgogo.py
from  selenium.webdriver.support.wait import WebDriverWait
from  appium import webdriver
class app01(object):
    def __init__(self):
        caps = {}
        caps['deviceName'] = '127.0.0.1:62001'
        caps['platformName'] = 'android'
        caps['platformVersion'] = '5.1.1'
        caps['appPackage'] = 'com.tencent.mobileqq'
        caps['appActivity'] = '.activity.SplashActivity'
        caps['noReset'] = True
        caps["unicodekeyboard"] = True
        caps["resetkeyboard"] = True
        self.driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', caps)
        self.driver.implicitly_wait(20)


    #定位
    def dingwei(self,locator):
        el = self.driver.find_element_by_xpath(locator)
        return el

        # 输入操作
    def shur(self, locator, test):
        el = self.dingwei(locator)
        el.send_keys(test)

        # 点击操作
    def click01(self, locator ):
        el = self.dingwei(locator)
        el.click()

    # 清除默认值
    def qingchu(self, locator):
        self.driver.find_element_by_xpath(locator).clear()

    # 显示等待
    def xianshidengdai(self, locator, text):
        WebDriverWait(self.driver, 10, 0.5).until(lambda el: self.driver.find_element_by_xpath(locator),
           message='text')


