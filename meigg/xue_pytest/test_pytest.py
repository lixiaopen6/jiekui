# -*- coding:utf-8 -*-
# @Time :2020/3/17 10:31
# @Email  :1084928753@qq.com
# @File :test_pytest.py
# import pytest,allure
import random,pytest,allure
print(random.randint(1,2))
@pytest.fixture(scope="function",autouse=True)
@allure.feature('登录接口')
def test_01():
    print("登录系统")


def test_02():
    print("用例2")


def test_03():
    print('接口用例3')




class TestCace():
   def test_04(self):
      print('接口用例4')

   def Test_03(self):
       print('接口用例5')


if __name__ == "__main__":
    # pytest.main(["-s", "test_pytest.py",'--html=./report/test.html','--maxfail=1'])
    pytest.main(["-s", '-q',"test_pytest.py", '--alluredir', './report/xml'])

