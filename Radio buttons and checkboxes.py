from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/")

#working  with radio buttons

#status=driver.find_element(By.ID,"RESULT_CheckBox-8_0").is_selected()

#driver.find_element(By.ID,"RESULT_CheckBox-8_0").click()
sta=driver.find_element(By.ID,"RESULT_CheckBox-8_0").is_selected()
print(sta)
#working checkboxes
driver.find_element(By.ID,"RESULT_CheckBox-9_0").click()
driver.find_element(By.ID,"RESULT_CheckBox-9_6").clear()
st=driver.find_element(By.ID,"RESULT_CheckBox-9_0").is_selected()
print(st)












