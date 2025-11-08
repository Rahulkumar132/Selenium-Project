from time import sleep

from selenium.webdriver import  Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get("https://opensource-demo.orangehrmlive.com/web/index.php/auth/login")
driver.maximize_window()
sleep(2)
driver.find_element(By.XPATH,'//input[@placeholder="Username"]').send_keys('Admin')
sleep(2)
driver.find_element(By.XPATH,'//input[@placeholder="Password"]').send_keys('admin123')
sleep(2)
driver.find_element(By.XPATH,'//button[@type="submit"]').click()
sleep(2)
driver.find_element(By.XPATH,'//span[.="Admin"]').click()
sleep(2)
driver.find_element(By.XPATH,'//span[.="My Info"]').click()
sleep(2)
driver.find_element(By.XPATH,'//input[@name="firstName"]').send_keys('Rahul')
sleep(2)
driver.find_element(By.XPATH,'//input[@name="lastName"]').send_keys('Kumar')
sleep(2)
driver.find_element(By.XPATH,'(//button[@type="submit"])[1]').click()
sleep(2)
