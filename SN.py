from selenium import webdriver

import time
driver = webdriver.Chrome()

driver.get("http://www.suning.com")

driver.maximize_window()
driver.find_element_by_link_text("请登录").click()
time.sleep(2)
driver.find_element_by_xpath('/html/body/div[2]/div[1]/div/div[1]/a[2]/span').click()
driver.find_element_by_id("userName").send_keys("15233003864")
driver.find_element_by_id("password").send_keys("LGQY1147")
time.sleep(3)
driver.find_element_by_xpath('//*[@id="iar1_sncaptcha_button"]/span').click()

driver.find_element_by_xpath('//*[@id="submit"]').click()






