from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
pracsite=driver.find_element_by_xpath("//a[text()='Practice Site']")
actions=ActionChains(driver)
actions.move_to_element(pracsite).click().perform()