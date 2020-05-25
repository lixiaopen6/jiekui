# -*- coding:utf-8 -*-
# @Time :2020/4/15 18:30
# @Email  :1084928753@qq.com
# @File :test_shouye.py
from ddt import  ddt,file_data,os,yaml
from meigg.UI.peizhiwenjbao.peizhi import dakai
import unittest

path=os.path.abspath(os.path.dirname(__file__))#获取文件当前位置
yamlpath1=path+'../yamlyaml\\url.yaml'#相对路径的yaml文件路径
yamlpath=r'C:\Users\Administrator\PycharmProjects\lix\meigg\yamlyaml\url.yaml'

def rr_yaml():
    with open(yamlpath, 'r', encoding='utf-8')as f :
        yyaml=yaml.load(f.read(),Loader=yaml.FullLoader)
    return yyaml

yaya=rr_yaml()
@ddt
class test_sss(unittest.TestCase):
    url=yaya['url']
    # 前置条件
    def setUp(self) -> None:
        print('开始测试')

    # 后置条件
    def tearDown(self) -> None:
        print('结束测试')
    @file_data('tada.yaml')
    def test_shouye(self,**info):
        self.username1='//*[@id="app"]/div/div/div/div/div/div/div/form/div[1]/input'  # username路径
        self.password1= '//*[@id="app"]/div/div/div/div/div/div/div/form/div[2]/input'  # password路径
        self.denglu= '//*[@id="app"]/div/div/div/div/div/div/div/form/button'  # 登录路径
        self.s = dakai(self.url)
        self.username=info.get('username')
        self.password = info.get('password')
        self.s.send_keys1(self.username1,self.username)
        self.s.send_keys1(self.password1,self.password)
        self.s.click1(self.denglu)
        # self.assertEqual()
        self.close01()

if __name__=='__main__':
    unittest.main()

