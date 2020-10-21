from selenium import webdriver
import time

driver = webdriver.Firefox()

driver.get('https://www.selenium.dev/selenium/docs/api/java/index.html')

driver.switch_to.frame('packageListFrame')  # First frame
driver.find_element_by_link_text('org.openqa.selenium').click()
time.sleep(3)

driver.switch_to.default_content()

driver.switch_to.frame('packageFrame')  # Second frame
driver.find_element_by_link_text('WebDriver').click()
time.sleep(3)
driver.switch_to.default_content()
time.sleep(3)
driver.switch_to.frame('classFrame')  # Third frame
driver.find_element_by_xpath('/html/body/div[1]/ul/li[5]').click()
