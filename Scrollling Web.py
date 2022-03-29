from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://www.countries-ofthe-world.com/flags-of-the-world.html")
driver.maximize_window() #maximize window
# Scroll down window page
#Types of Scrolling web page are :
#first one is execute as scroll based on Pixel
# driver.execute_script("window.scrollBy(0,1000)","")

#second one is scroll down page till the element is visblie
flag=driver.find_element(By.XPATH,"//*[@id='content']/div[2]/div[2]/table[1]/tbody/tr[19]/td[2]")
driver.execute_script("arguments[0],scrollIntoview();",flag)