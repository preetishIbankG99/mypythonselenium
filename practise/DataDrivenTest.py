from practise import XLUtils
from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com/")
driver.maximize_window()
path="C:\\Users\GUDU\PycharmProjects\pythonprojects\ExcelFile\DataDriven.xlsx"
rows=XLUtils.getRowCount(path,'Sheet1')
for r in range(2,rows+1):
    username=XLUtils.readData(path,"Sheet1",r,1)
    password=XLUtils.readData(path,"Sheet1",r,2)
    driver.find_element_by_id("txtUsername").send_keys(username)

    driver.find_element_by_id("txtPassword").send_keys(password)

    driver.find_element_by_id("btnLogin").click()

    if driver.title=="OrangeHRM":
        print("passed")
        XLUtils.writeData(path,"Sheet1",r,3,"passed")
        time.sleep(5)
        driver.find_element_by_xpath("//a[@id='welcome']").click()
        time.sleep(4)
        driver.find_element_by_xpath("//a[text()='Logout']").click()
    else:
        print("failed")
        XLUtils.writeData(path, "Sheet1", r, 3, "failed")