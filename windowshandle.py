from selenium import    webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("http://demo.automationtesting.in/Windows.html")
driver.find_element_by_xpath("/html/body/div[1]/div/div/div/div[2]/div[1]/a/button").click()
print(driver.current_window_handle)
handles=driver.window_handles
for handle in handles:
    driver.switch_to.window(handle)
    print(driver.title)
    if driver.title=="Frames&windows":
        driver.close()
driver.quit()

