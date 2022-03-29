from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("http://demo.automationtesting.in/FileDownload.html")
driver.maximize_window()
#download text file
driver.find_element(By.ID,"textbox").send_keys("hello alexa")
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div[2]/div[2]/button").click()
driver.find_element(By.XPATH,"/html/body/section/div[1]/div/div/div[2]/div[2]/a").click()
#download pdf file
driver.find_element(By.ID,"pdfbox").send_keys("hello alexa")
driver.find_element(By.ID,"pdfbox").click()
driver.find_element(By.ID,"pdf-link-to-download").click()
time.sleep(10)
driver.quit()




