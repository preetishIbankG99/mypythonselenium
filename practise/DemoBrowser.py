from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("http://demo.guru99.com/v4/")
# username=mngr321357
# password=bYhYsuh
print(driver.title)
driver.close()