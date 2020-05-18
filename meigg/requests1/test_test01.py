# -*- coding:utf-8 -*-
# @Time :2020/2/15 10:20
# @Email  :1084928753@qq.com
# @File :test_test01.py
import json
import requests
import unittest


class http(unittest.TestCase):
    url = 'http://39.107.96.138:3000/api/v1/'
    url1 = 'http://39.98.138.157:5001/api/'
    Token=''
    Topic_id=''
    accesstoken=' 00718f96-931c-4c8e-97d2-5f2b28b5a439'
    def setUp(self) -> None:
        pass
    def tearDown(self) -> None:
        pass
    def test001(self):#新增主题
        data = {"accesstoken": self.accesstoken,
                "title": "一二三四五六七",
                "tab": "ask",
                "content": "上山打老虎"}
        s = requests.post(self.url+'topics',data)
        r = s.json()
        http.Topic_id=r["topic_id"]
        print('第一个接口',s.url)
        print('第一个接口',s)
        print('第一个接口',s.json())
        print('第一个接口',http.Topic_id)
        self.assertTrue(r["success"])#判断success为True
        print(r["success"])


    def test002(self):#编辑主题
        data1 = {"accesstoken": self.accesstoken,
                 "topic_id": http.Topic_id,
                 "title": "六五四三二一",
                 "tab": "ask",
                 "content": "老虎不在家"}
        s = requests.post(self.url+'topics/update', data=data1)
        rr=s.json()
        print('第二个接口', s.url)
        print('第二个接口', s)
        print('第二个接口', s.json())
        self.assertTrue(rr["success"])  # 判断success为True
        # self.assertEqual(rr["Topic_id"]),http1.Topic_id,msg='修改失败')
        print(rr["success"])

    # def test003(self):#登录
    #     data = {"username": "admin", "password": "123456"}
    #     headers = {'Content-Type': 'application/json'}
    #     data = json.dumps(data)
    #     s = requests.post(self.url1+'login', data, headers=headers)
    #     ss=s.json()
    #     http1.Token=ss["token"]
    #     # self.assertEqual(self.Toke,'ewhrnkjdfdkjfkjf',msg='没登录')
    #     print('第一个接口',s.url)
    #     print('第一个接口',s)
    #     print('第一个接口',s.json())
    #     print('第一个接口',http1.Token)
    #
    # def test004(self):#获取用户列表
    #     headers1 = {"token": http1.Token}
    #     ss = requests.get(self.url1 + 'user/list', headers=headers1)
    #     print('第二个接口', ss.url)
    #     print('第二个接口', ss)
    #     print('第二个接口', ss.json())
    #     # self.assertEqual(self.Toke, 'ewhrnkjdfdkjfkjf', msg='没修改')


if __name__ == '__main__':
    unittest.main()
    import unittest
    import os
    from lianx.requests1.test_test01 import http
    from HTMLTestRunner_cn import HTMLTestRunner

    suite = unittest.TestSuite()#创建测试套件
    report_name = '小鹏的测试报告2020-3-6'
    report_title = '小鹏的测试报告2020-3-6'
    report_desc = '一灯老师要的，啥都有'
    report_path = './report/'  # 保存路径
    report_file = report_path + 'report5.html'  # 保存文件名称
    if not os.path.exists(report_path):  # 判断是否存在该文件夹
        os.mkdir(report_path)
    else:
        pass
    with open(report_file, 'wb')as report:  # 打开文件命名为report
        suite.addTest(unittest.TestLoader().loadTestsFromTestCase(http))  # 测试文件
        # 测试文件
        runner = HTMLTestRunner(stream=report, title=report_title, description=report_desc)
        runner.run(suite)
    report.close()

