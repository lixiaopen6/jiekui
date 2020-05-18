# -*- coding:utf-8 -*-
# @Time :2020/3/8 17:39
# @Email  :1084928753@qq.com
# @File :test_00000.py
import requests,unittest,json,yaml,os,logging
from HTMLTestRunner_cn import HTMLTestRunner
from lianx.requests1.httpjiek.httpjiek import jiek
from lianx.requests1.logginging.log import logger
ss=jiek()
class http(unittest.TestCase):
    # url = yaya['qqurl']['qqsurl']
    # url1 = yaya['qqurl']['qqsurl']
    Token = ''
    Topic_id = ''
    accesstoken = '25c46f78-525d-44bd-9cd0-2d988d3bdf2f'

    def test001(self):  # 新增主题
        data = {"accesstoken": self.accesstoken,
                 "title": "一二三四五六七",
                 "tab": "ask",
                 "content": "上山打老虎"}
        # s = requests.post(self.url, name='topics',data=data)
        # logger.info("第一个用例，接口地址{0},接口入参{1}，""入参类型{2}，接口状态码{3}，接口响应值{4}".
        #  format(self.url+'topics',data,type(data),s.status_code,s))
        # r = s.json()
        # http1.Topic_id = r["topic_id"]
        # self.assertTrue(r["success"])  # 判断success为True

        res=jiek.send_request(self,methon='post',name='topics',data=data,)
        # r = res.json()
        # http1.Topic_id = r["topic_id"]
        self.assertTrue(res["success"])  # 判断success为True
        self.jiancha({'success': True},res)
    def test002(self):  # 编辑主题
        data1 = {"accesstoken": self.accesstoken,
                 "topic_id": http.Topic_id,
                 "title": "六五四三二一",
                 "tab": "ask",
                 "content": "老虎不在家"}
        s = requests.post(self.url + 'topics/update', data=data1)
        # logger.info("第二个用例，接口地址{0},接口入参{1}，""入参类型{2}，接口状态码{3}，接口响应值{4}".
        #             format(self.url + 'topics', data1, type(data1), s.status_code, s))
        # rr = s.json()
        # self.assertTrue(rr["success"])  # 判断success为True
        # self.assertEqual(rr["Topic_id"]),http1.Topic_id,msg='修改失败')

    # def test003(self):#登录
    #     res=jiek()
    #     data = {"username": "admin", "password": "123456"}
    #     headers = {'Content-Type': 'application/json'}
    #     res= jiek.send_request(self,methon="post",name='login',data=data)
    #     self.assertEqual(res["msg"],'登录成功',msg='没登录')
    #     http1.Token=res["token"]
    #
    # def test004(self):#获取用户列表
    #     headers = {"token": self.Token}
    #     res = jiek.send_request(self,methon="get",name='user/list', headers=headers)
    #     # self.assertEqual(len(res["data"],2),)

    # def test005(self):
    #     pass

    def jiancha(self,yuqing,shiji):
        for key,value in yuqing.items():# key=name,value=admin
            if key in shiji:#预期值在实际返回值key里面
                self.assertEqual(value,shiji[key])
                logger.info('结果正确')
            else:#预期值不在实际返回值key里面
                for _key,_value in shiji.items():#循环res
                    if isinstance(_value,dict) and (key in _value) :#如果value是字典，而且在里面
                        # self.assertEqual(value,_value[key])
                        aa = {}
                        aa[key] = value
                        self.jiancha(aa, value)


if __name__ == '__main__':
    unittest.main()
    # sss=unittest.TestSuite()
    # sss.addTest(unittest.TestLoader().loadTestsFromTestCase(http1))
    # dir=r'C:\Users\Administrator\PycharmProjects\lix\lianx\requests1\report\jiek.html'
    # open1=open(dir,'wb')
    # runner=HTMLTestRunner(stream=open1,title='小二次元入口',description='首先你需要看懂这个一灯老师要的报告')
    # runner.run(sss)
