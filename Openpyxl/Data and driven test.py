import xlutils as XLUtils
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By


driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://demo.guru99.com/test/newtours")
driver.maximize_window()
path="D://Docments/test.xlsx"

rows=XLUtils.getRowCount(path,"sheet1")

for r in range(5):
    username=XLUtils.readData(path,"sheet1",r,1)
    password=XLUtils.readData(path,"sheet1",r,2)

driver.find_element(By.NAME,"userName").send_keys("Vikas")
driver.find_element(By.NAME,"password").send_keys("password")
driver.find_element(By.ID,"Login").click()

if driver.title=="Find the element:mercury tours:":
        print("test is passed")
        XLUtils.writeData(path,"sheet1",r,3,"TEST PASSED")
else:
    print("test case failed")
    XLUtils.writeData(path,"sheet1",r,3,"failed")
    driver.find_element(By.LINK_TEXT,"Home").click()


