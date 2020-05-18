# -*- coding:utf-8 -*-
# @Time :2020/2/24 11:52
# @Email  :1084928753@qq.com
# @File :appium1.py
from  appium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from appgogo import app01
driver=app01()
# driver.click01("//android.widget.Button[@resource-id='com.tencent.mobileqq:id/btn_login']")
# driver.shur("//android.widget.EditText[@text='QQ号/手机号/邮箱' and @content-desc='请输入QQ号码或手机或邮箱']",'2326268720')#账号
# driver.shur("//android.widget.EditText[@resource-id='com.tencent.mobileqq:id/password']",'13028811500mm')#密码
# driver.click01("//android.widget.ImageView[@resource-id='com.tencent.mobileqq:id/login']")#点击登录按钮
# driver.click01("//android.widget.TextView[@resource-id='com.tencent.mobileqq:id/dialogRightBtn']")#点击同意协议
# driver.click01("//android.widget.ImageView[@resource-id='com.tencent.mobileqq:id/login']")#点击登录按钮
# driver.click01("//android.widget.TextView[@resource-id='com.tencent.mobileqq:id/ivTitleBtnLeft']")
driver.click01("//android.widget.TabWidget[@resource-id='android:id/tabs']/android.widget.FrameLayout[3]/android.widget.RelativeLayout[1]/android.view.View[1]")#点击动态
driver.click01("//android.widget.TextView[@text='好友动态']")#点击好友动态
driver.click01("//android.widget.ImageView[@resource-id='com.tencent.mobileqq:id/dsr']")
driver.click01("//android.widget.LinearLayout[@resource-id='com.tencent.mobileqq:id/hp3']"
 "/android.widget.RelativeLayout[1]/android.widget.LinearLayout[1]/android.widget.FrameLayout[1]/android.widget.ImageView[1]")#点击说说
driver.shur("//android.widget.EditText[@resource-id='com.tencent.mobileqq:id/itv']",'666')#输入666
driver.click01("//android.widget.TextView[@resource-id='com.tencent.mobileqq:id/ivTitleBtnRightText']")#点击发表
print('搞定收工')





