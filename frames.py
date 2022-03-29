from selenium import webdriver
import time
driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://www.selenium.dev/selenium/docs/api/java/index.html")
driver.switch_to.frame("packageListFrame")
driver.find_element_by_link_text("org.openqa.selenium").click()

driver.switch_to.default_content()

driver.switch_to.frame("packageFrame")
driver.find_element_by_link_text("webdriver").click()

driver.switch_to.default_content()

driver.switch_to.frame("classFrame")
driver.find_element_by_xpath("/html/body/div[1]/ul/li[5]").click()
