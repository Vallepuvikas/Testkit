from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://www.tutorialspoint.com/about/about_careers.htm")
#Identify elements
l=driver.find_element(By.LINK_TEXT,"Team")
l.click()
#exepected coindition for explicit wait
w=WebDriverWait(driver,5)
w.until(EC.presence_of_element_located((By.TAG_NAME,'h1')))
s=driver.find_element(By.TAG_NAME,'h1')
#obtain text
t=s.text
print('Text is:'+t)
driver.quit()

