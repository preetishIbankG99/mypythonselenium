from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
driver.get("https://www.amazon.in")
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)

#add new cookie
cookie={'name':'Guducookie','value':'123456789'}
driver.add_cookie()
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
#delete cookie
driver.delete_cookie('Guducookie')
cookies=driver.get_cookies()
print(len(cookies))
print(cookies)
