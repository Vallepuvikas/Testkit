from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()
driver.switch_to.frame(0)
driver.find_element(By.ID,"RESULT_FileUpload-10").send_keys("C://Users/91916/Pictures/Screenshots/Screenshot (13).png")


