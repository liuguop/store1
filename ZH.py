from urllib import request
from selenium import webdriver
from cv2 import cv2
import random
import time
import pyautogui

# 打开谷歌浏览器
driver = webdriver.Chrome()
driver.get("https://www.zhihu.com")
driver.maximize_window()
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]').click()
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[2]/div/label/input').send_keys("15803422277")
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[3]/div/label/input').send_keys('ld199458')
time.sleep(2)
driver.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/button').click()

# # 获取图片信息，返回最佳匹配位置
def findPic(target="img1.jpg", template="img2.png"):
    # 读取图片
    target_rgb = cv2.imread(target)
    # 图片灰度化
    target_gray = cv2.cvtColor(target_rgb, cv2.COLOR_BGR2GRAY)
    # 读取模块图片
    template_rgb = cv2.imread(template, 0)
    # 匹配模块位置
    res = cv2.matchTemplate(target_gray, template_rgb, cv2.TM_CCOEFF_NORMED)
    # 获取最佳匹配位置
    value = cv2.minMaxLoc(res)
    # 返回最佳X坐标
    return value[2][0]

while True:
    try:
        # 从网页上获取组件

        target = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/img[1]')

        template = driver.find_element_by_xpath('/html/body/div[4]/div[2]/div/div/div[2]/div/div[1]/div/div[1]/img[2]')
        # 获取模块的url路径

        src1 = target.get_attribute("src")
        src2 = template.get_attribute("src")
        # 下载图片
        request.urlretrieve(src1,"img1.jpg")
        request.urlretrieve(src2,"img2.png")

        x = findPic()
        print(x)


        # 按钮坐标
        offset_x,offset_y = 795,573
        #pyautogui库操作鼠标指针
        pyautogui.moveTo(offset_x,offset_y,duration=0.1 + random.uniform(0,0.1 + random.randint(1,100) / 100))
        pyautogui.mouseDown()
        offset_y += random.randint(9,19)
        pyautogui.moveTo(offset_x + int(x * random.randint(20,23) / 20),offset_y,duration=0.28)
        offset_y += random.randint(-9,0)
        pyautogui.moveTo(offset_x + int(x * random.randint(19,23) / 20),offset_y,
                         duration=random.randint(20,31) / 100)
        offset_y += random.randint(0,8)
        pyautogui.moveTo(offset_x + int(x * random.randint(20,21) / 20),offset_y,
                         duration=random.randint(20,40) / 100)
        offset_y += random.randint(-3,3)
        pyautogui.moveTo(x + offset_x + random.randint(-3,3),offset_y,duration=0.5 + random.randint(-10,10) / 100)
        offset_y += random.randint(-2,2)
        pyautogui.moveTo(x + offset_x + random.randint(-2,2),offset_y,duration=0.5 + random.randint(-3,3) / 100)
        pyautogui.mouseUp()
        time.sleep(2)
        result = driver.find_element_by_xpath('//*[@id="JDJRV-wrap-loginsubmit"]/div/div/div/div[2]/div[3]').text
        if '不匹配' in result:
            print("账户名密码不匹配!", result)
            break
    except:
        print("异常!")
        break
