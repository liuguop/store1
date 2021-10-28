from selenium import webdriver

import time
driver = webdriver.Chrome()

driver.get("http://www.qcc.com")
#F:/自动化测试18/练习的html/弹框的验证/dialogs.html
driver.maximize_window()
driver.find_element_by_xpath('//*[@class="navi-btn login-nav-btn"]').click()
time.sleep(2)
driver.find_element_by_xpath('//*[@id="normalLogin"]').click()
driver.find_element_by_id("nameNormal").send_keys("15233003864")
driver.find_element_by_id("pwdNormal").send_keys("LGQY1147")
driver.find_element_by_xpath('//*[@id="user_login_normal"]/button/b').click()






