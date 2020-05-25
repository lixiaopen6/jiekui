print("conftestffff文件")

import pytest
from selenium import  webdriver
from POM.login import Login
from selenium.webdriver.common.by import By

import allure
@pytest.fixture()
def login(browser):
    pass
    '''登录函数:快递100'''
    print('开始调用登录')
    browser.find_element(*Login.username).send_keys('15902127953')  # 输入用户名
    try:
        browser.find_element(*Login.password).send_keys('test123456')  # 输入密码
    except Exception as e:

            file_name = r'C:\Users\Administrator\PycharmProjects\xue_pytest\png\peg2.PNG'
            browser.save_screenshot(file_name)  # 截图函数
            with open(file_name, mode='rb')as ff:
               f = ff.read()  # 读取文件将读取结果作为参数传给allure
            allure.attach(f, 'denglu', allure.attachment_type.PNG)#把图片添加到allure
            return e

    browser.find_element(*Login.denglu).click()  # 点击登录按钮
    yield browser
    browser.quit()
# class shouye(gonggo):
#     url='https://sso.kuaidi100.com/sso/authorize.do'
#     name=(By.XPATH,'//*[@id="name"]')
#     pwd=(By.XPATH,'//*[@id="password"]')
#     de=(By.XPATH,'//*[@id="submit"]')
#     test = "15902127953"
#     password = 'test123456'
#
#     #输入账号
#     def shur(self,text):
#         self.dingwei(self.name).send_keys(self.text)
#     #输入密码
#     def shur1(self,text):
#         self.dingwei(self.pwd).send_keys(self.password)
#     #点击登录
#     def click1(self):
#         self.dingwei(self.de).click()
#
#         self.quit()
#     #登录流程
#     def ddd(self,text,password):
#         self.shur(text)
#         self.shur1(password)
#         self.click1()
#         yield
#
# if __name__ == '__main__':
#     s=shouye('cc',shouye.url)
# #
# #
#

