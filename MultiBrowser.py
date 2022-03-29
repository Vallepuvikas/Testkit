from selenium import  webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://accounts.myherbalife.com/?appId=1&locale=en-US&redirect=https://www.myherbalife.com/")


print(driver.title)

driver.close()
