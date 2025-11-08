from time import sleep

from selenium.webdriver import  Chrome, ChromeOptions
from selenium.webdriver.common.by import By

#from selenium.webdriver.common.by import By

o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)
#driver.get("file:///C:/Users/rk570/OneDrive/Desktop/Selenium%20html/rahul.html")
driver.maximize_window()
sleep(2)
#Locator values matches exactly with single element
#finding the element address
'''
un=driver.find_element(By.ID,'a1')
un.send_keys('rahul@gmail.com')
sleep(2)
'''
#finding the element and performing action on same line
'''driver.find_element(By.ID,'a1').send_keys('rahul@gmail.com')'''
#if the locator match with multiple element then find_element will return first element address
'''
pwd=driver.find_element(By.ID,'a1')
pwd.send_keys('rahul@kumar')
sleep(2)
'''

#if the locator  values not matches  with any element then find_element will throw #NoSuchElementException
'''pwd=driver.find_element(By.ID,'a10')
pwd.send_keys('rahul@kumar')
sleep(2)
#o/p
#NoSuchElementException'''


#write script  to login the facebook
'''driver.get('https://www.fb.com')
driver.find_element(By.ID,'email').send_keys('rahulkumar@gmai.com')
driver.find_element(By.ID,'pass').send_keys('rahul123')
driver.find_element(By.ID,'loginbutton').click()
'''
#example on facebook
'''driver.get('http://127.0.0.1:5500/Controll%20Stetment/built%20in%20method%20in%20list/self/rahul.html')
driver.maximize_window()
sleep(2)
driver.find_element(By.LINK_TEXT,'Facebook').click()'''


'''driver.get('https://www.facebook.com/')
driver.maximize_window()
sleep(2)'''
'''driver.find_element(By.LINK_TEXT,'Create a Page').click()
sleep(2)
driver.find_element(By.LINK_TEXT,'Forgotten password?').click()
sleep(2)
'''

driver.get('http://127.0.0.1:5500/Controll%20Stetment/built%20in%20method%20in%20list/self/rahul.html')
driver.maximize_window()
sleep(2)
driver.find_element(By.CSS_SELECTOR,"input[type='text']").send_keys('Rshulkumar@123')
sleep(2)
driver.find_element(By.ID,"a2").send_keys('Rshulkuma2')
sleep(2)




