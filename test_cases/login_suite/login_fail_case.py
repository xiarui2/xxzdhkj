import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
from common import set_driver
from common import login
current = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current,'../../webdriver/chromedriver')
class LoginFailCase(unittest.TestCase):
    def setUp(self) -> None:#把selenium的初始化配置放入
        self.driver = set_driver.set_driver()
    def tearDown(self) -> None:#关闭浏览器
        time.sleep(2)
        self.driver.quit()
    def test_login_03(self):
        '''case03 使用test01 newdream12 测试能否登录'''
        login.login(self.driver,'test01','newdream12')
        self.assertTrue( WebDriverWait(self.driver,10).until(EC.alert_is_present()))#此断言的意思：判断页面上是否有alter弹窗，如果有就切换到alter并返回alter的内容


if __name__ == "__main__":
    unittest.main()



















