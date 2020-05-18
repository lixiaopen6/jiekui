# -*- coding:utf-8 -*-
# @Time :2020/3/5 16:50
# @Email  :1084928753@qq.com
# @File :suite.py
import unittest
import os
from requests1.test_test01 import http
from HTMLTestRunner_cn import HTMLTestRunner
suite=unittest.TestSuite()
report_name='小鹏的测试报告2020-3-5'
report_title='小鹏的测试报告2020-3-5'
report_desc='一灯老师要的，啥都有'
report_path='./report/'   #保存路径
report_file=report_path+'report4.html'  #保存文件名称
if not os.path.exists(report_path):    #判断是否存在该文件夹
    os.mkdir(report_path)
else:
    pass
with open(report_file, 'wb')as report:     #打开文件命名为report
    suite.addTest(unittest.TestLoader().loadTestsFromTestCase(http))#测试文件
      #测试文件
    runner=HTMLTestRunner(stream=report,title=report_title,description=report_desc)
    runner.run(suite)
report.close()
