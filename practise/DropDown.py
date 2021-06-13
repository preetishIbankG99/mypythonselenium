from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://www.seleniumeasy.com/test/basic-select-dropdown-demo.html")
element=driver.find_element_by_xpath("//select[@class='form-control']")
drp=Select(element)

drp.select_by_visible_text("Wednesday")
time.sleep(4)
drp.select_by_index(6)

