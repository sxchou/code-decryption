from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
import time
driver = Edge()
driver.get('https://mail.qq.com/')
driver.switch_to.frame('login_frame')
driver.find_element(By.XPATH, '//*[@id="u"]').send_keys('qq账号')
driver.find_element(By.XPATH, '//*[@id="p"]').send_keys('qq密码..')
time.sleep(3)
driver.find_element(By.XPATH, '//*[@id="login_button"]').click()
