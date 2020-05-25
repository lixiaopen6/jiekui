# -*- coding:utf-8 -*-
# @Time :2020/3/19 11:27
# @Email  :1084928753@qq.com
# @File :test_03-15.py
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# import pytest
# from time import sleep
#
# driver = webdriver.Chrome()
# # def chushihua():
# #     driver.get("http://39.98.138.157/shopxo/index.php")
# #     driver.implicitly_wait(10)
# #     driver.maximize_window()
# @pytest.fixture()
# def denglu():
#     driver.get("http://39.98.138.157/shopxo/index.php")
#     driver.implicitly_wait(10)
#     driver.maximize_window()
#     driver.find_element_by_link_text('登录').click()#点击登录
#     driver.find_element_by_xpath('//*[@placeholder="用户名/手机/邮箱"]').send_keys('testuser01')
#     driver.find_element_by_xpath('//*[@placeholder="登录密码"]').send_keys('123456')
#     driver.find_element_by_xpath('/html/body/div[4]/div/div[2]/div[2]/form/div[3]/button').click()#点击登录
#     WebDriverWait(driver,10,0.5).until\
#     (lambda el:driver.find_element_by_xpath('/html/body/div[2]/div/ul[1]/div/div/em[2]'),message='没登录')
#     yield denglu
# class test_tttt():
#
#     def test_sousuo(self,denglu):
#         denglu.find_element_by_xpath('//*[@placeholder="其实搜索很简单^_^ !"]').send_keys('一灯老师')
#         denglu.find_element_by_id('ai-topsearch').click()
#         # WebDriverWait(driver, 10, 0.5).until \
#         #     (lambda el: driver.find_element_by_link_text('没有相关品牌'), message='搜索失败')
#         sleep(2)
#         driver.close()
#
#     def test_shouji(self,denglu):
#         ele=denglu.find_element_by_link_text("数码办公")
#         ActionChains(driver).move_to_element(ele).perform()#鼠标悬停
#         denglu.find_element_by_xpath('//a[@title="手机"]/span').click()
#         WebDriverWait(driver, 10, 0.5).until \
#             (lambda el: driver.find_element_by_xpath()
#             ('/html/body/div[4]/div/ul/li[1]/div/a/img'), message='没进手机选择页面')
#
#         driver.find_element_by_xpath('/html/body/div[4]/div/ul/li[2]/div/a/img').click()#点击手机图片进入详情
#
# if __name__ == "__main__":
#     pytest.main(["-s", "test_03-15.py"])
#
#
#
#






