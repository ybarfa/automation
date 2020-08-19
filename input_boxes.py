from selenium import webdriver
from selenium.webdriver.common.by import By
import time
driver=webdriver.Chrome(executable_path="D:\\softwares\\gekodriver/\chromedriver.exe")

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

# how to find how many inputboxes are present in web pages

inputboxes=driver.find_elements(By.CLASS_NAME,'text_field')
print(len(inputboxes))

# How to get the status

status=driver.find_element(By.ID,'RESULT_TextField-1').is_displayed()
print("Displayed or not:", status)  # gives either True/False

status=driver.find_element(By.ID,'RESULT_TextField-1').is_enabled()
print("enabled or not:", status)

# How to provide value into text box



driver.find_element(By.ID,'RESULT_TextField-1').send_keys("yash")
driver.find_element(By.ID,'RESULT_TextField-2').send_keys("barfa")
driver.find_element_by_id('RESULT_TextField-3').send_keys("1234567890")
time.sleep(5)
driver.close()