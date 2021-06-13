from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
#1st
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)
#2nd
driver.get("http://demo.guru99.com/v4/")
print(driver.title)
print(driver.current_url)
time.sleep(4)
driver.back()
#1st
print(driver.title)
print(driver.current_url)
time.sleep(4)
driver.forward()
#2nd
print(driver.title)
print(driver.current_url)