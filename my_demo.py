from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
driver=webdriver.Chrome(executable_path="d:\softwares\gekodriver\chromedriver.exe")

driver.implicitly_wait(5)

driver.maximize_window()

driver.get('https://www.expedia.com/')

driver.find_element_by_xpath('//*[@id="uitk-tabs-button-container"]/li[2]/a').click()

time.sleep(2)

driver.find_element_by_xpath('//*[@id="wizard-flight-tab-roundtrip"]/div/div[1]/div/div[1]/div/div/div/button[1]').send_keys('Indore (IDR-Devi Ahilyabai Holkar Intl.)')


driver.close()