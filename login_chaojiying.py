from selenium.webdriver import Edge
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from chaojiying import Chaojiying_Client
import time
driver = Edge()
driver.get('http://www.chaojiying.com/')
driver.find_element(By.XPATH, '//*[@id="carousel-example-generic"]/div/div[1]/article/a[2]').click()
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[1]/input').send_keys('超级鹰账号')
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[2]/input').send_keys('超级鹰密码')
img = driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/div/img').screenshot_as_png
chaojiying = Chaojiying_Client('超级鹰账号', '超级鹰密码', '96001')
dic = chaojiying.PostPic(img, 1902)
verify_code = dic['pic_str']
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[3]/input').send_keys(verify_code)
time.sleep(3)
driver.find_element(By.XPATH, '/html/body/div[3]/div/div[3]/div[1]/form/p[4]/input').click()
time.sleep(3)
