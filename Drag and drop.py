from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("http://www.dhtmlgoodies.com/scripts/drag-drop-custom/demo-drag-drop-3.html")
driver.maximize_window()

source_element=driver.find_element(By.XPATH,"//*[@id='box7']")
des_element=driver.find_element(By.XPATH,"//*[@id='box106']")
action=ActionChains(driver)

action.drag_and_drop(source_element,des_element)