from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get("https://mail.google.com/mail/u/0/?tab=rm&ogbl#inbox" )
driver.maximize_window()
'''driver.find_element(By.XPATH,'//a[.="Gmail"]').click()
sleep(3)
driver.find_element(By.XPATH,'//input[@type="email"]').send_keys('rahulkumar.qa9@gmail.com')
sleep(3)
driver.find_element(By.XPATH,'//span[.="Next"]').click()
sleep(3)'''



