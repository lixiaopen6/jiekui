import time
from POM.login import Login
class TestLogin():
    def test00(self,browser):
        browser.find_element(*Login.username).send_keys('15277807977')  # 输入用户名
        # browser.find_element(*Login.password).send_keys('')  # 输入密码
        browser.find_element(*Login.denglu).click()  # 点击登录按钮
        browser.quit()

    def test01(self,login):
        time.sleep(3)
        login.find_element_by_xpath("//a[text()='我的快递号']").click()  # 搜索
        time.sleep(5)
        print("用例二执行之前需要登录")


