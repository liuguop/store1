from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get(r"C:\Users\刘\Desktop\Jason python\自动化测试1\练习的html\上传文件和下拉列表\autotest.html")
#F:/自动化测试18/练习的html/上传文件和下拉列表/autotest.html
driver.maximize_window()

# driver.find_element_by_id("accountID") 局限性
driver.find_element_by_xpath("//*[@id='accountID']").send_keys("jason jia")
driver.find_element_by_xpath("//*[@id='passwordID']").send_keys("admin")
driver.find_element_by_xpath("//*[@id='areaID']").send_keys("天津市")
#北京市
time.sleep(2)
driver.find_element_by_xpath("//*[@id='sexID1']").click()
#sexID2
driver.find_element_by_xpath("//*[@value='summer']").click()
#spring
driver.find_element_by_xpath("//*[@value='winter']").click()
#Auterm
driver.find_element_by_xpath("//*[@name='file' and @type='file']").send_keys(r"D:\背景2.jpg")
#C:\Users\jason\Pictures\picture.jpg
driver.find_element_by_xpath("//*[@id='buttonID']").click()
driver.switch_to.alert.accept()