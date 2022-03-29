from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import  By

driver=webdriver.Chrome(executable_path="D:\Downloads\chromedriver_win32 (2)\chromedriver.exe")
driver.get("https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407/")
Element=driver.find_element(By.ID,"RESULT_RadioButton-7")
drp=Select(Element)
#select by visble text
drp.select_by_visible_text('Morning')

#select by index
drp.select_by_index(2)
#select by value
drp.select_by_value("Radio-2")
#count number of options
print(len(drp.options))
#capture all the options and print them as output
all_options=drp.options

for option in all_options:
    print(option.text)

