# -*- coding:utf-8 -*-
# @Time :2020/3/5 10:49
# @Email  :1084928753@qq.com
# @File :api_api.py
import requests,unittest,json,yaml,os,logging
from HTMLTestRunner_cn import HTMLTestRunner
# from lianx.requests1.httpjiek.peizhiwenj import jiek

path=os.path.abspath(os.path.dirname(__file__))#获取文件当前位置
yamlpath=path+'\yamlyaml\\tada.yaml'#相对路径的yaml文件路径
def rr_yaml():
    with open(yamlpath, 'r', encoding='utf-8')as f :
    # vvyaml=open(yamlpath, 'r', encoding='utf-8')
    # yyaml=yaml.load(vvyaml,Loader=yaml.FullLoader)
       yyaml=yaml.load(f.read())
    return yyaml
yaya=rr_yaml()


class http(unittest.TestCase):
    url = yaya['url']
    url1 = yaya['qqurl']['qqsurl']
    Token = ''
    Topic_id = ''
    accesstoken = '80a37434-bd74-4920-86ff-d633bb6c8979'


    def test001(self):  # 新增主题
        data = {"accesstoken": self.accesstoken,
                 "title": "一二三四五六七",
                 "tab": "ask",
                 "content": "上山打老虎"}
        # s = requests.post(self.url, name='topics',data)
        # logger.info("第一个用例，接口地址{0},接口入参{1}，""入参类型{2}，接口状态码{3}，接口响应值{4}".
        #  format(self.url+'topics',data,type(data),s.status_code,s))
        # r = s.json()
        # http1.Topic_id = r["topic_id"]
        # self.assertTrue(r["success"])  # 判断success为True

        res=self.send_request('post',name='topics',data=data,)
        self.assertTrue(res["success"])  # 判断success为True
    # def test002(self):  # 编辑主题
    #     data1 = {"accesstoken": self.accesstoken,
    #              "topic_id": http1.Topic_id,
    #              "title": "六五四三二一",
    #              "tab": "ask",
    #              "content": "老虎不在家"}
    #     # s = requests.post(self.url + 'topics/update', data=data1)
    #     # logger.info("第二个用例，接口地址{0},接口入参{1}，""入参类型{2}，接口状态码{3}，接口响应值{4}".
    #     #             format(self.url + 'topics', data1, type(data1), s.status_code, s))
    #     # rr = s.json()
    #     self.assertTrue(rr["success"])  # 判断success为True
    #     # self.assertEqual(rr["Topic_id"]),http1.Topic_id,msg='修改失败')

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
    #
    # def test005(self):
    #     pass




if __name__ == '__main__':
    # unittest.main()
    sss=unittest.TestSuite()
    sss.addTest(unittest.TestLoader().loadTestsFromTestCase(http))
    dir=r'C:\Users\Administrator\PycharmProjects\lix\lianx\requests1\report\jiek.html'
    open1=open(dir,'wb')
    runner=HTMLTestRunner(stream=open1,title='小二次元入口',description='首先你需要看懂这个一灯老师要的报告')
    runner.run(sss)

