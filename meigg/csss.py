# -*- coding:utf-8 -*-
# @Time :2020/5/11 9:44
# @Email  :1084928753@qq.com
# @File :csss.py
import time
from flask import Flask
xinxin=Flask(__name__)

@xinxin.route('/')
def hello():
    sentence = "520"
    for char in sentence.split():
        allChar = []
        for y in range(12, -12, -1):
            lst = []
            lst_con = ''
            for x in range(-30, 30):
                formula = ((x * 0.05) ** 2 + (y * 0.1) ** 2 - 1) ** 3 - (x * 0.05) ** 2 * (y * 0.1) ** 3
                if formula <= 0:
                    lst_con += char[(x) % len(char)]
                else:
                    lst_con += ' '
            lst.append(lst_con)
            allChar += lst
        print('\033[0;32m' + '\n'.join(allChar) + '\033[0m')  # 设置字体颜色和背景


    return ('\033[0;32m' + '\n'.join(allChar) + '\033[0m')


if __name__ == '__main__':
    #运行服务，并确定服务运行的IP和端口
    xinxin.run('127.0.0.1','9090')


