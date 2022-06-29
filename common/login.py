from selenium.webdriver.common.by import By
import os
def login(driver,username,passwd):
    driver.find_element(By.CSS_SELECTOR, 'input#account').send_keys(username)
    driver.find_element(By.CSS_SELECTOR, 'input[name="password"]').send_keys(passwd)
    driver.find_element(By.CSS_SELECTOR, 'button.btn.btn-primary').click()