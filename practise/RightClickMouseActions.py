from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("http://testautomationpractice.blogspot.com/")
driver.maximize_window()
clickele=driver.find_element_by_xpath("//*[@id='HTML10']/div[1]/button")
actions=ActionChains(driver)
actions.context_click(clickele).perform()