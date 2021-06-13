from selenium import webdriver
from selenium.webdriver.common.keys import Keys
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
print(driver.title)
print(driver.current_url)

userele=driver.find_element_by_id("txtUsername")
print(userele.is_enabled())
userele.send_keys("Admin")
userpass=driver.find_element_by_id("txtPassword")
print(userpass.is_displayed())
userpass.send_keys("admin123")
driver.find_element_by_id("btnLogin").click()

driver.close()