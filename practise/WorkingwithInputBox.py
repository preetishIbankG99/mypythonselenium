from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
inputboxes=driver.find_elements(By.CLASS_NAME,'textInputContainer')
print(len(inputboxes))
status=driver.find_element(By.ID,'txtUsername').is_displayed()
print("Displayed or not:",status)

status=driver.find_element(By.ID,'txtUsername').is_enabled()
print("Enabled or not:",status)
driver.find_element(By.ID,'txtUsername').send_keys("Admin")
driver.find_element(By.ID,'txtPassword').send_keys("admin123")