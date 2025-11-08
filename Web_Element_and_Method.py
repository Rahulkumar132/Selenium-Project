from time import sleep
from typing import final

from selenium.webdriver import  Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get("https://www.google.com/")
driver.maximize_window()
sleep(2)
'''un=driver.find_element(By.XPATH,"//input[@name='email']")
un.send_keys('rahulkumar@gmail.com')
sleep(2)
un.clear()
sleep(2)
un.send_keys('rahulkumar132@')
sleep(2)
un=driver.find_element(By.XPATH,'//button[@name="login"]')
un.click()'''

#get_attribute_method
'''ele=driver.find_element(By.XPATH,'(//div[.="Log in to Facebook"])[2]')
data=ele.get_attribute('class')
print(data)
em=driver.find_element(By.XPATH,'//input[@name="email"]')
data1=em.get_attribute('placeholder')
print(data1)
em1=driver.find_element(By.XPATH,'//input[@id="email"]')
data2=em1.get_attribute('class')
print(data2)
'''
#write script for Tool Tip of voice icon in google.com
voice=driver.find_element(By.XPATH,'(//div[@role="button"])[2]')
data=voice.get_attribute('aria-label')
print(data)

