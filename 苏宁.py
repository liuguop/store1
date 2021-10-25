from selenium import webdriver


driver = webdriver.Chrome()

driver.get("http://suning.com")
#F:/自动化测试18/练习的html/弹框的验证/dialogs.html
# driver.maximize_window()
driver.find_element_by_xpath("//*[@id='searchKeywords']").send_keys("iphone13")
driver.find_element_by_id("searchSubmit").click()

driver.find_element_by_xpath('//*[@src="//image.suning.cn/uimg/pcms/label05/670677245207133719912800_11.png"]').click()

new_win=driver.window_handles[-1]
driver.switch_to.window(new_win)

driver.find_element_by_id("addCart").click()


# driver.switch_to.alert.accept()  #accept()  确定
# driver.switch_to.alert.dismiss() # 取消