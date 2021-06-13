from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
from selenium.webdriver import ActionChains

driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
driver.find_element_by_xpath("//input[@type='file']").send_keys("C://Users/GUDU/Desktop/a060558eafea469381357d13fccf632c.txt")
