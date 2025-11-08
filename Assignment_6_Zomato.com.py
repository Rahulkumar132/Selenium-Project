from time import sleep
from typing import final

from selenium.webdriver import  Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get('https://www.zomato.com/bangalore/thyme-whisk-uttarahalli-bangalore/order')
driver.maximize_window()
sleep(2)
un1=driver.find_element(By.XPATH,'//a[.="Sign up"]')
un1.click()
un2=driver.find_element(By.XPATH,'(//span[.="Create account"])[1]')
print(un2.is_enabled())
sleep(2)
