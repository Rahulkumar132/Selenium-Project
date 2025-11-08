from time import sleep

from selenium.webdriver import  Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get("https://www.irctc.co.in/nget/train-search")
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
sleep(2)
driver.find_element(By.CLASS_NAME,"fa.fa-align-justify").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"button[class='search_btn']").click()
sleep(2)
driver.find_element(By.LINK_TEXT,"REGISTER").click()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
sleep(2)
driver.find_element(By.ID,"userName").send_keys('rahulkumar@122')
sleep(2)
driver.find_element(By.ID,"fullName").send_keys('Rahul Kumar')
sleep(2)
driver.find_element(By.ID,"usrPwd").send_keys('Rahulkumar124@4')
sleep(2)
driver.find_element(By.ID,"cnfUsrPwd").send_keys('Rahulkumar124@4')
sleep(2)
driver.find_element(By.ID,"email").send_keys('rk5700@gmail.com')
sleep(2)
driver.find_element(By.ID,"mobile").send_keys('7541921901')
sleep(2)
driver.find_element(By.ID,"captcha").send_keys('rjgh8w')
sleep(2)
driver.find_element(By.CSS_SELECTOR,"button[type='submit']").click()
sleep(2)








