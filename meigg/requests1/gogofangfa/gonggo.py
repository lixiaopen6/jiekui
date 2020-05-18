# -*- coding:utf-8 -*-
# @Time :2020/3/11 11:53
# @Email  :1084928753@qq.com
# @File :gonggo.py
'''封装公共方法，yaml,mysql等'''
import logging,yaml,os,pymysql

# path=os.path.abspath(os.path.dirname(__file__))#获取文件当前位置
# print(path)
# yamlpath=path+'\yamlyaml\\tada.yaml'#相对路径的yaml文件路径
yamlpath=r'C:\Users\Administrator\PycharmProjects\lix\meigg\requests1\yamlyaml\tada.yaml'
def rr_yaml():
    # with open(yamlpath,'r',encoding='utf-8') as f:
        vvyaml=open(yamlpath, 'r', encoding='utf-8')
        yyaml=yaml.load(vvyaml,Loader=yaml.FullLoader)
    #     yyaml=yaml.load(f.read())
    #     print(type(yyaml),yyaml)
        return yyaml
def connect_mysql():
    # db_connect=pymysql.connect(host='',port='3306',user='',password='')
    # cursor=db_connect.cursor()
    # cursor.execute(sql)
    # res=cursor.fetchall()
    res=''
    return  res