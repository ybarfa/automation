from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://fs2.formsite.com/meherpavan/form2/index.html?1537702596407')

# Working with the radio button

status = driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected()  # True/False
print(status)

driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').click()  # Select radio button
time.sleep(5)
status = driver.find_element_by_xpath('//*[@id="q26"]/table/tbody/tr[1]/td/label').is_selected()   # True/False
print(status)


# Working with checkboxes

driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[1]/td/label').click()
driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[2]/td/label').click()
driver.find_element_by_xpath('//*[@id="q15"]/table/tbody/tr[5]/td/label').click()

time.sleep(3)
driver.close()
