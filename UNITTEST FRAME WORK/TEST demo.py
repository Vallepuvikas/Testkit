import unittest
from selenium import webdriver

class SearchEnginesTest(unittest.TestCase):
    def test_Google(self):
        self.driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
        self.driver.get("https://google.com")
        print("Title of page :" +self.driver.title)

    def test_bing(self):
        self.driver = webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
        self.driver.get("https://google.com")
        print("Title of page in bing:" + self.driver.title)

if __name__=="__main__":
    unittest.main()

