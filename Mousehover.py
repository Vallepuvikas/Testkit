from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://opensource-demo.orangehrmlive.com")
driver.find_element(By.XPATH,"//*[@id='txtUsername']").send_keys("Admin")
driver.find_element(By.XPATH,"//*[@id='txtPassword']").send_keys("admin123")
driver.find_element(By.XPATH,"/html/body/div[1]/div/div[3]/div[2]/div[2]/form/div[5]/input").click()

#Using on actionchains
admin=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewAdminModule']/b")
usermnt=driver.find_element(By.XPATH,"//*[@id='menu_admin_UserManagement']")
driver.implicitly_wait(10)
user=driver.find_element(By.XPATH,"//*[@id='menu_admin_viewSystemUsers']")

action=ActionChains(driver)
action.move_to_element(admin).move_to_element(usermnt).move_to_element(user).click().perform()

