from time import sleep
from selenium.webdriver import Chrome,ChromeOptions
from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
driver.get('https://www.youtube.com/')
driver.maximize_window()
sleep(2)
'''driver.find_element(By.XPATH,'//input[@name="search_query"]').send_keys('testingbyrahul')
sleep(3)
driver.find_element(By.XPATH,'//button[@aria-label="Search"]').click()
sleep(3)
driver.find_element(By.XPATH,'//yt-formatted-string[.="Google clouds "]').click()
sleep(3)
driver.find_element(By.XPATH,'(//a[@href="/watch?v=bsEravb4fPg"])[3]').click()
sleep(3)'''
driver.find_element(By.XPATH,'//a[@aria-label="You"]').click()
sleep(3)

driver.find_element(By.XPATH,'//a[@aria-label="Shorts"]').click()
sleep(3)
driver.find_element(By.XPATH,'//span[.="Subscriptions"]').click()
sleep(3)
driver.find_element(By.XPATH,'(//button[@id="button"])[2]').click()
sleep(3)
driver.find_element(By.XPATH,'//yt-formatted-string[.="History"]').click()
sleep(3)
driver.find_element(By.XPATH,'(//yt-formatted-string[.="YouTube Studio"])[1]').click()
sleep(3)


