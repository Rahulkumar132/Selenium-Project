from time import sleep
from selenium.webdriver import  Chrome, ChromeOptions
o=ChromeOptions()
o.add_experimental_option('detach',True)

#Write a script to return TITLE,CURRENT URL AND SOURCE CODE OF BROWSER
'''
driver=Chrome(options=o)
driver.maximize_window()
sleep(2)
driver.get("https://go.cloudskillsboost.google/arcade")
sleep(4)

#title property
print(driver.title)
sleep(2)

#current_url Property
print(driver.current_url)
sleep(2)

#page_source property
print(driver.page_source)
sleep(2)
'''