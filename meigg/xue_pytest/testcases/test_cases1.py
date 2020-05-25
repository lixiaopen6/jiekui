# -*- coding:utf-8 -*-
# @Time :2020/4/1 16:35
# @Email  :1084928753@qq.com
# @File :test_cases1.py
import requests,json,yaml
from httpfa import httpfa
class TestCase():
    print("test")
    def setup(self):
        print("test1")
        self.s=httpfa()
    def  test01(self):
        print("test2")
        test={"username":"admin","password":"123456"}
        print(test)
        res=self.s.send_request(method="post",name='login',data=test)
        assert res['httpstatus']==200

    def test02(self):
        data={}
        headers={"token":"camaxueyuan"}
        res=self.s.send_request(method="get",name='user/list',data=data,headers=headers)
        assert res['code']=='000'



if __name__ == "__main__":
    import pytest
    pytest.main(["-s","-vv",'test_cases1.py','--html=../report/test1.html'])










