
from selenium import webdriver
import time      # 导入下拉选项
from selenium.webdriver.common.action_chains import ActionChains   # 移动鼠标
driver = webdriver.Chrome()     # 创建浏览器
driver.maximize_window()        # 屏幕最大化
driver.get("https://www.bilibili.com//")    # 打开bibi登录网页
driver.implicitly_wait(2)

driver.find_element_by_xpath('//*[@id="internationalHeader"]/div/div/div[3]/div[2]/span[1]/div/span/div').click()
handle = driver.window_handles         # 获取所有页面 或 手柄
driver.switch_to.window(handle[1])     # 切换到第一个页面

#  登录bibi网站
driver.find_element_by_xpath("//*[@id='login-username']").send_keys("15233003864")
driver.find_element_by_xpath("//*[@id='login-passwd']").send_keys("LGQY1147")
driver.find_element_by_xpath('//*[@id="geetest-wrap"]/div/div[5]/a[1]').click()
time.sleep(10)

ele = driver.find_element_by_link_text("主站")    # 鼠标要移动的位置
Ac = ActionChains(driver)                        # 把控制交给 ActionChains
Ac.move_to_element(ele).perform()                # 鼠标移动到ele位置并立即执行
driver.find_element_by_xpath('//*[@id="internationalHeader"]/div/div/div[1]/ul/li[1]/span/a').click()
driver.implicitly_wait(2)
time.sleep(10)
driver.find_element_by_xpath('//*[@id="nav_searchform"]/input').send_keys("鬼畜")
driver.find_element_by_xpath('//*[@id="nav_searchform"]/div/button').click()
time.sleep(3)
handle = driver.window_handles
driver.switch_to.window(handle[2])
driver.implicitly_wait(2)
driver.find_element_by_xpath('//*[@id="all-list"]/div[1]/div[2]/ul/li[7]/a/div/div[1]/img').click()
handle = driver.window_handles
driver.switch_to.window(handle[3])
time.sleep(60)
driver.quit()