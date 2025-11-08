#Write  a script to perform backword , forward and refresh action in browser
from time import sleep
from selenium.webdriver import  Chrome, ChromeOptions
o=ChromeOptions()
o.add_experimental_option('detach',True)

#Write  a script to perform backword , forward and refresh action in browser
'''
driver=Chrome(options=o)
driver.maximize_window()
sleep(2)
driver.get("https://go.cloudskillsboost.google/arcade")
sleep(4)

#back() 
driver.back()
sleep(2)

#forward() 
driver.forward()
sleep(2)

#refresh()
driver.refresh()
sleep(2)
'''

#write a  script to return width , height x and y axis of the  Browser
'''
driver=Chrome(options=o)
driver.maximize_window()
sleep(2)
driver.get("https://go.cloudskillsboost.google/arcade")
sleep(2)

#get_window_size() 
res1=driver.get_window_size()
print(res1)
sleep(2)

#get_window_position()
res2=driver.get_window_position()
print(res2)
sleep(2)

#get_window_rect()
res3=driver.get_window_rect()
print(res3)
sleep(2)
'''

#write a script to resize the browser base on the x,y,height and width
'''
driver=Chrome(options=o)
driver.maximize_window()
sleep(2)
driver.get("https://go.cloudskillsboost.google/arcade")
sleep(2)

#set_window_size()
driver.set_window_size(99,77)
sleep(2)

#set_window_position()
driver.set_window_position(44,88)
sleep(2)

#set_window_rect()
driver.set_window_rect(33,55,88,99)
sleep(2)
'''

