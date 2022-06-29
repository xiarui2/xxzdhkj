import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC

current = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current,'../../webdriver/chromedriver')
class LoginSuccessCase(unittest.TestCase):
    def setUp(self) -> None:#把selenium的初始化配置放入
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    def tearDown(self) -> None:#关闭浏览器
        time.sleep(2)
        self.driver.quit()
    def test_login_1(self):
        '''case1 使用test01 newdream123 测试能否登录'''
        self.driver.find_element(By.CSS_SELECTOR,'input#account').send_keys('test01')
        self.driver.find_element(By.CSS_SELECTOR,'input[name="password"]').send_keys('newdream123')
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
        actual_result = self.driver.find_element(By.CSS_SELECTOR, 'span.user-name').text  # 获取文本值
        self.assertEqual(actual_result, 'test01', 'test_login用例执行失败')
        # self.assertEqual(EC.text_to_be_present_in_element(By.CSS_SELECTOR,'span.user-name'),'test01')

    def test_login_2(self):
        '''case2 使用test02 newdream123 测试能否登录'''
        self.driver.find_element(By.CSS_SELECTOR,'input#account').send_keys('test02')
        self.driver.find_element(By.CSS_SELECTOR,'input[name="password"]').send_keys('newdream123')
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
        actual_result = self.driver.find_element(By.CSS_SELECTOR,'span.user-name').text#获取文本值
        self.assertEqual(actual_result,'测试人员2','test_login用例执行失败')

if __name__ == "__main__":
    unittest.main()
















