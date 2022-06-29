import os,time
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

current = os.path.dirname(__file__)
chrome_driver_path = os.path.join(current,'../../webdriver/chromedriver')
class MenuLinkCase(unittest.TestCase):
    def setUp(self) -> None:#把selenium的初始化配置放入
        self.driver = webdriver.Chrome(executable_path=chrome_driver_path)
        self.driver.implicitly_wait(10)
        self.driver.maximize_window()
        self.driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
        self.driver.find_element(By.CSS_SELECTOR, 'input#account').send_keys('test01')
        self.driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys('newdream123')
        self.driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()
    def tearDown(self) -> None:#关闭浏览器
        time.sleep(2)
        self.driver.quit()
    def test_my_link(self):
        '''case04 验证我的地盘菜单能否正确链接'''
        self.driver.find_element(By.CSS_SELECTOR,'li[data-id="my"]').click()
        self.assertTrue(EC.title_is('我的地盘 - 禅道'))

    def test_product_link(self):
        '''case05 验证产品菜单能否正常链接'''
        self.driver.find_element(By.CSS_SELECTOR,'li[data-id="product"]').click()
        self.assertTrue(EC.title_is('产品主页 - 禅道'))



if __name__ == "__main__":
    unittest.main()



















