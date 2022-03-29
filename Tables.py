from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Ie(executable_path="C:\IEDriverServer_Win32_4.0.0\IEDriverServer.exe")
driver.get("https://demo.guru99.com/test/web-table-element.php")
rows=driver.find_element(By.XPATH,"/html/body/div/div[3]/div[1]/table/thead/tr/th[1]")
cols=driver.find_element(By.XPATH,"/html/body/div/div[3]/div[1]/table/thead/tr/th[2]")

print(rows)
print(cols)

print("product"+"   "+"Article"+"   "+"Price")
for r in range(2):
    for c in range(1):
        value=driver.find_element(By.XPATH,"/html/body/div/div[3]/div[1]/table/tbody/tr[7]/td[1]").text
        print(value,end="  ")
    print()
