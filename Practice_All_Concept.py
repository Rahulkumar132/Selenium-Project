#write script to launch the empty Chrome Browser
'''
from selenium.webdriver import Chrome
c=Chrome()
'''
from time import sleep

from cffi.cffi_opcode import CLASS_NAME
from selenium.webdriver.common.by import By

#write script to launch the empty Edge Browser
'''
from selenium.webdriver import Edge
e=Edge()
'''

#write script to launch the empty Firefox Browser
'''
from selenium.webdriver import Firefox, FirefoxProfile
f=Firefox()
'''
from selenium.webdriver import Chrome, ChromeOptions
o=ChromeOptions()
o.add_experimental_option('detach',True)
driver=Chrome(options=o)

#write  a script to enter the URL
'''
driver.get('https://www.facebook.com')
driver.get('https://www.youtube.com/@testingbyrahul')
driver.get('http://www.youtube.com/@testingbyrahul')
driver.get('www.youtube.com/@testingbyrahul')
'''
#write a script for maximize,minimize and fullscreen the window
#from time import sleep
'''
driver.maximize_window()
sleep(4)
driver.minimize_window()
sleep(2)
driver.fullscreen_window()
'''
#driver.close()
#Write  a script to perform backword , forward and refresh action in browser
'''driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.back()
sleep(2)
driver.forward()
sleep(2)
driver.refresh()
sleep(3)'''

#write a script to resize the browser base on the x,y,height and width
'''driver.get('https://www.amazon.in/')
driver.maximize_window()
r=driver.get_window_size()
print(r)
sleep(2)
r1=driver.get_window_position()
print(r1)
sleep(2)
r2=driver.get_window_rect()
print(r2)
sleep(2)

'''
'''driver.get('https://www.amazon.in/')
driver.maximize_window()
driver.set_window_size(55,88)
sleep(2)
driver.set_window_position(77,33)
sleep(2)
driver.set_window_rect(33,55,99,88)

'''
driver.get('https://www.zomato.com/bangalore/delivery')
driver.maximize_window()
sleep(2)
driver.find_element(By.CLASS_NAME,'sc-3o0n99-5.jqszCs').click()
sleep(2)
driver.find_element(By.CLASS_NAME,'sc-kAyceB.iRZJkq').click()
un=driver.find_element(By.CLASS_NAME,'sc-kAyceB.iRZJkq')
un.click()






