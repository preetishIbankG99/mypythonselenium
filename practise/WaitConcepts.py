from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.implicitly_wait(10)
assert "OrangeHRM" in driver.title
driver.find_element_by_xpath("//input[@name='txtUsername']").send_keys("Admin")

driver.find_element_by_xpath("//input[@name='txtPassword']").send_keys("admin123")

