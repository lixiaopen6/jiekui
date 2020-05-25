from selenium.webdriver.common.by import By
from ddt import ddt,unpack,file_data,data

class Login():
    username=(By.XPATH,'//*[@id="name"]')
    password=(By.XPATH,'//*[@id="password"]')
    denglu=(By.XPATH,'//*[@id="submit"]')
    zhanghao=(By.XPATH,'15902127953')
    mima=(By.XPATH,'test123456')




    # 元素定位
    def dingwei(self, locator):
        el = self.driver.find_element(*locator)
        return el

    #输入账号
    def shur(self,text):
        self.dingwei(self.username).send_keys(self.zhanghao)
    #输入密码
    def shur1(self,text):
        self.dingwei(self.password).send_keys(self.password)
    #点击登录
    def click1(self):
        self.dingwei(self.denglu).click()
        self.quit()
    #登录流程
    def ddd(self,text,password):
        self.shur(text)
        self.shur1(password)
        self.click1()
        yield








