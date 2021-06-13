from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-radiobutton-demo.html")
status=driver.find_element_by_xpath("(//input[@value='Male'])[1]").is_selected()
print(status)
driver.find_element_by_xpath("(//input[@value='Male'])[1]").click()
status=driver.find_element_by_xpath("(//input[@value='Male'])[1]").is_selected()
print(status)

driver.get("https://www.seleniumeasy.com/test/basic-checkbox-demo.html")
status1=driver.find_element_by_xpath("(//input[@type='checkbox' ]) [2]").is_selected()
print(status1)
driver.find_element_by_xpath("(//input[@type='checkbox' ]) [2]").click()
print(status1)

status1=driver.find_element_by_xpath("(//input[@type='checkbox' ]) [5]").is_selected()
print(status1)
driver.find_element_by_xpath("(//input[@type='checkbox' ]) [5]").click()
print(status1)