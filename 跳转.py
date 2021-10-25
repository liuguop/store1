from selenium import webdriver
#跳转页面的测试
import time
driver = webdriver.Chrome()
# driver.get(r"C:\Users\刘\Desktop\Jason python\自动化测试1\练习的html\跳转页面\pop.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='goo']").click()


#输入框的测试
# driver.get(r"C:\Users\刘\Desktop\Jason python\自动化测试1\练习的html\frame.html")
# driver.maximize_window()
# driver.find_element_by_xpath("//*[@id='input1']").send_keys("123456")


driver.get(r"C:\Users\刘\Desktop\Jason python\自动化测试1\练习的html\main.html")

f = driver.find_element_by_id("frame")
driver.switch_to.frame(f)
time.sleep(2)
driver.find_element_by_id("input1").send_keys("123344")
# time.sleep(5)
# driver.quit()