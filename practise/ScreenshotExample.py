from selenium import webdriver

driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
#driver.save_screenshot("C://Users/GUDU/PycharmProjects/pythonprojects/Screenshots/homepage.png")
driver.get_screenshot_as_file("C:\\Users\GUDU\PycharmProjects\pythonprojects\Screenshots\homepage.png")