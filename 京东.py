from selenium import webdriver
import time

driver = webdriver.Chrome()

driver.get("http://www.jd.com")
#F:/自动化测试18/练习的html/弹框的验证/dialogs.html
# driver.maximize_window()
time.sleep(2)
driver.find_element_by_xpath("//*[@id='key']").send_keys("iphone13")
driver.find_element_by_class_name("button").click()

# driver.find_element_by_id("J_searchWrap").click()
driver.find_element_by_xpath('//*[@src="//img12.360buyimg.com/n7/jfs/t1/197266/19/11794/111930/615ea5a4E48c0e85c/3adcb6562e8f4767.jpg"]').click()
#
# #切换窗口
new_win=driver.window_handles[-1]
driver.switch_to.window(new_win)
# #加入购物车
driver.find_element_by_id("InitCartUrl").click()



# driver.switch_to.alert.accept()  #accept()  确定
# # driver.switch_to.alert.dismiss() # 取消
# import time
# from selenium import webdriver
# from selenium.webdriver import ActionChains
# from selenium.webdriver.support.select import Select
#
# driver=webdriver.Chrome()
# driver.implicitly_wait(10)
# driver.maximize_window()
# #打开京东
# driver.get("https://www.jd.com/")
# #点击登陆
# driver.find_element_by_class_name("link-login").click()
# driver.find_element_by_link_text("账户登录").click()
# #登录账号记得删掉
# driver.find_element_by_id("loginname").send_keys("158**03")
# driver.find_element_by_id("nloginpwd").send_keys("c**")
# driver.find_element_by_css_selector(".btn-img.btn-entry").click()
# #手动滑验证图片
# time.sleep(5)
# #输入要购买的信息
# driver.find_element_by_id("key").send_keys("桔子")
# driver.find_element_by_class_name("button").click()
# #点击第一个商品
# # driver.find_element_by_id("J_AD_6111576").click()
# driver.find_element_by_xpath('//*[@id="J_goodsList"]/ul/li[1]/div/div[1]/a/img').click()
# #切换窗口
# new_win=driver.window_handles[-1]
# driver.switch_to.window(new_win)
# #加入购物车
# driver.find_element_by_id("InitCartUrl").click()
# #点购物车结算
# driver.find_element_by_id("GotoShoppingCart").click()
# #点结算
# driver.find_element_by_class_name("submit-btn").click()
# #点新增收货地址
# driver.find_element_by_css_selector(".ftx-05.J_consignee_global").click()
# #点击新增收货地址后，跳转到frame
# driver.switch_to.frame("dialogIframe")
# #等待
# time.sleep(3)
# #鼠标悬停在所在地区处
# element=driver.find_element_by_xpath('//*[@id="jd_area"]/div[1]/div')
# ActionChains(driver).move_to_element(element).perform()
# #鼠标点击浙江省
# script="document.getElementsByClassName('ui-switchable-panel')[0].style.display = null"
# driver.execute_script(script)
# driver.find_element_by_xpath('//*[@id="jd_area"]/div[2]/div[2]/div/ul/li[15]/a').click()
# #鼠标点击宁波
# script="document.getElementsByClassName('ui-switchable-panel')[1].style.display = null"
# driver.execute_script(script)
# driver.find_element_by_xpath('//*[@id="jd_area"]/div[2]/div[2]/div[2]/ul/li[1]/a').click()
# #鼠标点击北仑区
# script="document.getElementsByClassName('ui-switchable-panel')[2].style.display = null"
# driver.execute_script(script)
# driver.find_element_by_xpath('//*[@id="jd_area"]/div[2]/div[2]/div[3]/ul/li[1]/a').click()
# #鼠标点击白峰镇
# driver.find_element_by_xpath('//*[@id="jd_area"]/div[2]/div[2]/div[4]/ul/li[1]/a').click()
