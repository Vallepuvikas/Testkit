from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.find_element_by_xpath("//*[@ID='HTML9']/div[1]button").click()
time.sleep(5)
driver.switch_to_alert.dismiss() 
