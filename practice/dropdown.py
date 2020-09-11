from selenium import webdriver
from selenium.webdriver.support.ui import Select
import time

driver=webdriver.Chrome(executable_path="D:\\softwares\\gekodriver/\chromedriver.exe")

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

element=(driver.find_element_by_id('RESULT_RadioButton-9'))
drp=Select(element)

# select by visible text
drp.select_by_visible_text('Morning') #Morning

time.sleep(5)

# select by index
drp.select_by_index(2) #Afternoon

time.sleep(5)

#Select by value
drp.select_by_value('Radio-2') #Evening

time.sleep(5)

#Count number of options

print(len(drp.options))

#Capture all the options and print them as output

all_options=drp.options

for option in all_options:
    print(option.text)

driver.quit()