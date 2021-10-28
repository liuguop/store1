# from selenium import webdriver
# import time
# # import datetime
#
#
# # 自动登录
# def aoto_login(username, password):
#     default_url = 'https://www.taobao.com/'  # 默认使用淘宝网址
#     driver.get(default_url)
#     driver.find_element_by_link_text('亲，请登录').click()
#     time.sleep(3)
#     login_name = driver.find_element_by_name('fm-login-id')
#     login_name.send_keys(username)
#     login_password = driver.find_element_by_name('fm-login-password')
#     login_password.send_keys(password)
#     login_button = driver.find_element_by_class_name('fm-btn')
#     login_button.click()
#     print('自动登录成功')


# 抢购（purchase_url：待抢购商品的链接；）
# def buy(purchase_url, purchase_times):
#     driver.get(purchase_url)
#     for i in range(1):
#         now = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S.%f')
#         print('当前时间{0}'.format(now))
#         if now >= purchase_times:
#             if driver.find_element_by_class_name('tb-btn-buy'):
#                 driver.find_element_by_class_name('tb-btn-buy').click()
#                 # 提交订单
#                 driver.find_element_by_link_text('【10月】核桃味24盒').click()
#                 driver.find_element_by_class_name('ensureText').click()
#                 time.sleep(2)
#                 driver.find_element_by_class_name('go-btn').click()
#         time.sleep(0.01)

#
# if __name__ == "__main__":
#     driver = webdriver.Chrome()  # 打开浏览器
#     driver.maximize_window()  # 浏览器窗口最大化
#     username = '15233003864'  # 账号
#     password = 'LGQY1147'  # 密码
#     aoto_login(username=username, password=password)  # 淘宝自动化登录
    # 待抢购商品链接
    # url = 'https://detail.tmall.com/item.htm?spm=a230r.1.14.29.e8d7147d12inmO&id=623689464704&ns=1&abbucket=4'
    # # 抢购时间倒计时
    # times = '2020-12-12 16:18:00.000000'  # 抢购倒计时时间（时间格式："2018-09-06 11:20:00.000000"）
    # buy(purchase_url=url,purchase_times=times)  # 开始抢购





from selenium import webdriver
import time
from selenium.webdriver.common.action_chains import ActionChains
driver = webdriver.Chrome()

driver.get("http://taobao.com")
#F:/自动化测试18/练习的html/弹框的验证/dialogs.html
driver.maximize_window()

driver.find_element_by_link_text("亲，请登录").click()
# driver.implicitly_wait(2)
driver.find_element_by_id("fm-login-id").send_keys("15233003864")
driver.find_element_by_id("fm-login-password").send_keys("LGQY1147")
time.sleep(2)

ac = ActionChains(driver)
ele = driver.find_element_by_id("nc_1_n1z") # 滑块元素
ac.click_and_hold(ele).move_by_offset(300,0).perform()# 立即执行

ac.release()
# driver.find_element_by_class_name("fm-button fm-submit password-login fm-button-disabled").click()
