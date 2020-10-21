from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()

driver.get('https://www.facebook.com/')

links = driver.find_elements(By.TAG_NAME, "a")
print("Number of links present:", len(links))   # Print how many links present in a page

for link in links:
    print(link.text)

# Clicking on the link

# driver.find_element(By.PARTIAL_LINK_TEXT,"Developers").click()

driver.find_element(By.LINK_TEXT, "Developers").click()
