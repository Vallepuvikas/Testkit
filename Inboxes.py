from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/")

#How to find how many inboxes are presented in webpage
inputboxes=driver.find_element(By.CLASS_NAME,'text_field')
print(len("inputboxes"))
#How to provide data in text_fields
driver.find_element(By.NAME,"RESULT_TextField-1").send_keys("Vallepu")
driver.implicitly_wait(10)
driver.find_element(By.NAME,"RESULT_TextField-2").send_keys("Vikas")
driver.find_element(By.NAME,"RESULT_TextField-3").send_keys("9160673390")
driver.find_element(By.NAME,"RESULT_TextField-4").send_keys("India")
driver.find_element(By.NAME,"RESULT_TextField-5").send_keys("Anantapur")
driver.find_element(By.NAME,"RESULT_TextField-6").send_keys("Vikasvallepu@yahoo.com")
time.sleep(10)
driver.quit()







