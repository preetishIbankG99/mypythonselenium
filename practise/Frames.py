from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("http://demo.guru99.com/test/guru99home/")
driver.maximize_window()
driver.switch_to_frame("a077aa5e")
img=driver.find_element_by_xpath("/html/body/a/img")
img.click()
driver.switch_to_default_content()