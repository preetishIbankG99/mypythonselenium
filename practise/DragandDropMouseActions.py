from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
drag=driver.find_element_by_xpath("//p[text()='Drag me to my target']")
drop=driver.find_element_by_xpath("//p[text()='Drop here']")
actions=ActionChains(driver)
actions.drag_and_drop(drag,drop).perform()