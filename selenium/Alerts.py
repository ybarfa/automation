from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get("http://testautomationpractice.blogspot.com/")

driver.find_element_by_xpath('//*[@id="HTML9"]/div[1]/button').click()

time.sleep(5)

# driver.switch_to.alert.accept() #Closses alerts window using OK button

driver.switch_to.alert.dismiss()  # Closes alerts by using Cancel button

time.sleep(5)

driver.close()
