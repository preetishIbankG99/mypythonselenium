from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import selenium.webdriver.WebDriverWait
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.maximize_window()
driver.get("https://opensource-demo.orangehrmlive.com/")
time.sleep(4)
driver.find_element_by_xpath("//input[@name='txtUsername']").send_keys("Admin")
#wait=WebDriverWait(driver,10)
#userpass=wait.until(EC._element_if_visible((By.XPATH,"//input[@name='txtPassword']")))
