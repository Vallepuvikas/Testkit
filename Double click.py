from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://testautomationpractice.blogspot.com/")
driver.maximize_window()

element=driver.find_element(By.XPATH,"//*[@id='HTML10']/div[1]/button")
action=ActionChains(driver)
action.double_click(element).perform()