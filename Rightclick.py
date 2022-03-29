from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://swisnl.github.io/jQuery-contextMenu/demo.html")
driver.maximize_window()
button=driver.find_element(By.XPATH,"/html/body/div/section/div/div/div/p/span")
action=ActionChains(driver)
action.context_click(button).perform()
