import time

class TestLogin():

    def test01(self,login):
        print('这是用例一')
        time.sleep(3)
        login.find_element_by_xpath("//a[text()='地址管理']").click()  # 搜索

        time.sleep(5)

