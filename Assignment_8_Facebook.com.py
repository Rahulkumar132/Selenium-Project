from time import sleep

from select import select
from selenium.webdriver import  Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get("https://www.facebook.com/")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'(//a[@role="button"])[2]').click()
sleep(2)
driver.find_element(By.XPATH,'//input[@name="firstname"]').send_keys('Rahul')
sleep(2)
driver.find_element(By.XPATH,'//input[@name="lastname"]').send_keys('kumar')
sleep(2)
d=driver.find_element(By.XPATH,'//select[@aria-label="Day"]')
data=Select(d)
data.select_by_index(5)
sleep(2)
d1=driver.find_element(By.XPATH,'//select[@aria-label="Month"]')
data1=Select(d1)
data1.select_by_index(5)
sleep(2)
d2=driver.find_element(By.XPATH,'//select[@aria-label="Year"]')
data2=Select(d2)
data2.select_by_index(23)
sleep(2)
driver.find_element(By.XPATH,'(//input[@type="radio"])[2]').click()
sleep(2)
driver.find_element(By.XPATH,'//input[@name="reg_email__"]').send_keys('rk5700177@gmail.com')
sleep(2)
driver.find_element(By.XPATH,'//input[@type="password"]').send_keys('rk5500@133')
sleep(2)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
sleep(2)








