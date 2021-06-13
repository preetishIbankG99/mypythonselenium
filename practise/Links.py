from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://www.seleniumeasy.com/")
links=driver.find_elements(By.TAG_NAME,"a")
print("Number of links present:",len(links))
for link in links:
    print(link.text)
    driver.find_element(By.LINK_TEXT,"Selenium").click()