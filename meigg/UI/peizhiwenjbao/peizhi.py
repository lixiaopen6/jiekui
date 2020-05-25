# -*- coding:utf-8 -*-
# @Time :2020/4/8 17:59
# @Email  :1084928753@qq.com
# @File :peizhi.py
import os
import random

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait

current_path=os.path.abspath(os.path.dirname(__file__))#获取文件当前位置
print(current_path)
class  dakai():
    def __init__(self,url):
        self.liulanq(url)

    def liulanq(self,url):
        self.open_url(url)

    def open_url(self,url):
        self.driver=webdriver.Chrome()
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
    # 定位元素
    def dingwei(self,locator):
            el = self.driver.find_element_by_xpath(locator)
            return el
     #输入内容
    def send_keys1(self,locator,test):
        self.dingwei(locator).clear()
        el=self.dingwei(locator)
        el.send_keys(test)

    # 点击
    def click1(self,locator):
        el=self.dingwei(locator)
        el.click()
    #切换句柄，保留原页面
    def switch_handle(self):
        handles=self.driver.window_handles
        self.driver.switch_to.window(handles[1])

    # 切换句柄，删除原页面
    def swith_handle_del(self):
        handles = self.driver.window_handles
        self.driver.close()
        self.driver.switch_to.window(handles[1])

    # 关闭页面
    def close01(self):
        self.driver.close()

    # 清除默认值
    def qingchu(self, locator):
        self.driver.find_element_by_xpath(locator).clear()

     #显示等待
    def xianshidengdai(self,locator,text):
        WebDriverWait(self.driver,10,0.5).until(lambda el:self.driver.find_element_by_xpath(locator),message='text')

    def phone_nobo(self,top=None):
        '''获取随机手机号码'''
        if not top:
            phone_list = ['136', '188', '134', '135', '184', '187', '183']  # 定义号码段
            phone = random.choice(phone_list) + "".join(random.choice("0123456789") for _ in range(8))
        else:
            phone = str(top) + "".join(random.choice("0123456789") for _ in range(8))
        return phone

    def random_name(self):
        '''随机名字'''
        import random as r

        a1 = ['张', '金', '李', '王', '赵']

        a2 = ['玉', '明', '龙', '芳', '军', '玲']

        a3 = ['', '立', '玲', '', '国', '']

        for i in range(15):
            name = r.choice(a1) + r.choice(a2) + r.choice(a3)
            return name


    def connect_mysql(sql):
        '''查询数据库的过程'''
        # db_connect=pymysql.connect(host='',port='3306',user='',password='')
        # cursor=db_connect.cursor()
        # cursor.execute(sql)
        # res=cursor.fetchall()
        res = 'admin'
        return res

    # from ruamel import yaml
    # current_path=os.path.abspath(os.path.dirname(__file__))#获取文件当前位置
    #
    # def write_yaml(self,extract_dict):  #写入yaml 文件方法
    #     with open(current_path+'\config\extract.yaml','w') as f:
    #         yaml.dump(extract_dict, f, Dumper=yaml.RoundTripDumper)
    #
    # def read_yaml(self):
    #     with open(current_path,'r',encoding='utf-8') as f:
    #         cfg=yaml.load(f,Loader=yaml.RoundTripLoader,preserve_quotes=True)
    #         #print(type(cfg),cfg)
    #         return cfg
    #
    # def read_yaml_extract(self,data):   #读写 yaml文件方法
    #     '''cematoken:'''
    #     with open(current_path+'\config\extract.yaml','r',encoding='utf-8') as f:
    #         cfg=yaml.load(f,Loader=yaml.RoundTripLoader,preserve_quotes=True)
    #         data=cfg[data]
    #         #print(type(cfg),cfg)
    #         return data














