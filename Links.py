from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("http://newtours.demoaut.com.cutestat.com/")
links=driver.find_element(By.TAG_NAME,'a')
print("number of links present:",len("links"))
for links in link:
    print(link.text)

