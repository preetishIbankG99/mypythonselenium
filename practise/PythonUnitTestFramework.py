import unittest
from selenium import webdriver
class SearchEngineTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
        self.driver.get("http://www.google.com/")
        print("Title of page is :"+self.driver.title)
        self.driver.close()

    def test_Orangehrm(self):
      self.driver = webdriver.Chrome( executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
      self.driver.get("https://opensource-demo.orangehrmlive.com/")
      print("Title of page is :" + self.driver.title)
      self.driver.close()

    if __name__=="__main__":
                unittest.main()