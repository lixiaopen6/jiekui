# -*- coding:utf-8 -*-
# @Time :2020/3/24 16:46
# @Email  :1084928753@qq.com
# @File :conftest.py
print('根目录的conftest',11111111111)
from ddt import ddt ,file_data
import pytest,unittest
from selenium import  webdriver
# from login.log import logger
from selenium.webdriver.common.by import By
import allure
# @pytest.fixture()
# def  browser():
#     '''浏览器初始化'''
#     options=webdriver.ChromeOptions()
#     '''谷歌的headlens模式'''
#     options.add_argument('headless')
#     options.add_argument('start-maximized')
#     browser = webdriver.Chrome(options=options)  # 浏览器对象，实例化对象
#     browser.get('https://sso.kuaidi100.com/sso/authorize.do')
#     browser.maximize_window()
#     browser.implicitly_wait(10)
#     return browser
#
#
# def jietu(*aa):
#     file_name = r'C:\Users\Administrator\PycharmProjects\lix\meigg\png1\peg.png'
#     browser.save_screenshot(file_name)  # 截图函数
#     with open(file_name, mode='rb')as ff:
#        f = ff.read()  # 读取文件将读取结果作为参数传给allure
#     allure.attach(f, 'denglu', allure.attachment_type.PNG)#把图片添加到allure
#
# def baocuo(*aa):
#     try:
#           pass
#     except Exception as e:
#         file_name = r'C:\Users\Administrator\PycharmProjects\lix\meigg\png1\peg2.PNG'
#         browser.save_screenshot(file_name)  # 截图函数
#         with open(file_name, mode='rb')as ff:
#            f = ff.read()  # 读取文件将读取结果作为参数传给allure
#         allure.attach(f, 'denglu', allure.attachment_type.PNG)#把图片添加到allure
#         return e


