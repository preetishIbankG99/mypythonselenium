import unittest
from selenium import webdriver
class Test(unittest.TestCase):
    def test_Google(self):
     driver=webdriver.Chrome(executable_path="C:/Users/GUDU/PycharmProjects/pythonprojects/Drivers/chromedriver.exe")
     driver.get("http://www.google.com/")
     titleOfWebPage=driver.title
     self.assertEqual("Google",titleOfWebPage,"webpage title is not same")
        #self.assertNotEquals("Google123",titleOfWebPage)



    if __name__ == "__main__":
            unittest.main()