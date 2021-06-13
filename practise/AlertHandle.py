from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("http://www.seleniumeasy.com/test/javascript-alert-box-demo.html")
alert=driver.find_element_by_xpath("//button[@class='btn btn-default']")
alert.click()
print(driver.switch_to_alert().text)
driver.switch_to_alert().accept()
dismissalert=driver.find_element_by_xpath("(//button[@class='btn btn-default btn-lg'])[1]")
dismissalert.click()
driver.switch_to_alert().dismiss()