from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("http://demo.automationtesting.in/Register.html")
driver.maximize_window()
#scroll down page by pixel
#driver.execute_script("window.scrollBy(0,1000)","")
#scroll for certail element
#flag=driver.find_element_by_xpath("//*[@id='footer']/div/div/div[2]/a[4]")
#driver.execute_script("arguments[0].scrollIntoView();",flag)
#flag.click()
#scroll down page till end
driver.execute_script("window.scrollBy(0,document.body.scrollHeight)")