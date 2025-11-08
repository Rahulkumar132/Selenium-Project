from time import sleep

from selenium.webdriver import  Chrome, ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get("https://portal2.passportindia.gov.in/AppOnlineProject/user/RegistrationBaseAction?request_locale=en")
driver.maximize_window()
sleep(2)
driver.find_element(By.ID,'cpvLocation13').click()
sleep(2)
driver.find_element(By.ID,'givenName').send_keys('Rahul')
sleep(2)
driver.find_element(By.ID,'surname').send_keys('Kumar')
sleep(2)
driver.find_element(By.ID,'email').send_keys('rahulkumar.qa9@gmail.com')
sleep(2)
driver.find_element(By.ID,'emailloginSameyes').click()
sleep(2)
driver.find_element(By.ID,'loginId').send_keys('rahulkumar.qa9@gmail.com')
sleep(2)
driver.find_element(By.ID,'pwd').send_keys('rahulkumar@132')
sleep(2)
driver.find_element(By.ID,'confirmPwd').send_keys('rahulkumar@132')
sleep(2)
driver.find_element(By.ID,'hintAns').send_keys('city')
sleep(2)
driver.find_element(By.ID,'test123').send_keys('HRE345')
sleep(2)
driver.find_element(By.ID,'frmSample_register').click()
sleep(2)









