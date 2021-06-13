import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def test_Google(self):
     driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
     #it will pass if driver=None otherwise fail
     #self.assertIsNone(driver)
     self.assertIsNotNone(driver)
     if __name__ == "__main__":
         unittest.main()