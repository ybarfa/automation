from selenium import webdriver

driver = webdriver.Chrome(executable_path="D:\\softwares\\gekodriver\\chromedriver.exe")
driver.get("https://www.facebook.com/")
driver.find_element_by_xpath('//*[@id="email"]').send_keys('barfayash2@gmail.com')
driver.find_element_by_xpath('//*[@id="pass"]').send_keys('barfa@yash123')
driver.find_element_by_xpath('//*[@id="u_0_f"]').click()

driver.close()
