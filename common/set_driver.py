from selenium import webdriver
import os

def set_driver():
    current = os.path.dirname(__file__)
    chrome_driver_path = os.path.join(current, '../webdriver/chromedriver')
    driver = webdriver.Chrome(executable_path=chrome_driver_path)
    driver.implicitly_wait(10)
    driver.maximize_window()
    driver.get('http://47.107.178.45/zentao/www/index.php?m=user&f=login')
    return driver