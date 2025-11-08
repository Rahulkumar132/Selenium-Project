# Launch MakeMyTrip, click on bus, click on from and enter bangalore and click on bangalore, enter to as
# mangalore select  tomorrow date click on search buses , click on select seats, select any seat and proceed further

from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.by import By
from time import sleep

o = ChromeOptions()
o.add_experimental_option('detach', True)

driver = Chrome(options = o)
driver.get('https://www.makemytrip.com/')
driver.maximize_window()
sleep(1)
driver.fullscreen_window()
sleep(2)
driver.find_element(By.XPATH,'//span[@data-cy="closeModal"]').click()
sleep(4)
driver.find_element(By.XPATH,'//li[@class="menu_Buses"]').click()
sleep(4)
driver.find_element(By.XPATH,'//input[@data-cy="fromCityVal"]').click()
sleep(1)
driver.find_element(By.XPATH,'//input[@placeholder="From"]').send_keys('Bangalore, Karnataka')
sleep(2)
driver.find_element(By.XPATH,'//span[.="Bangalore, Karnataka"]').click()
sleep(2)
driver.find_element(By.XPATH,'//input[@placeholder="To"]').send_keys('mangalore')
sleep(2)
driver.find_element(By.XPATH,'//span[.="Mangaluru (Mangalore), Karnataka"]').click()
sleep(2)
driver.find_element(By.XPATH,'//div[@aria-label="Sat Nov 08 2025"]').click()
sleep(5)
driver.find_element(By.XPATH,'//button[.="Search"]').click()
sleep(2)
driver.find_element(By.XPATH,'//button[.="Select Seats"]').click()
sleep(2)
driver.find_element(By.XPATH,'//img[@alt="HORIZONTAL_SLEEPER"]').click()
sleep(2)
