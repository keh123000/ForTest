import cv2

import time
import requests
from selenium import webdriver
from selenium.webdriver import ActionChains

sleep = time.sleep


def get_track(distance):
    track = []
    current = 0
    mid = distance * 3 / 4
    t = 0.2
    v = 0
    while current < distance:
        if current < mid:
            a = 2
        else:
            a = -3
        v0 = v
        v = v0 + a * t
        move = v0 * t + 1 / 2 * a * t * t
        current += move
        track.append(round(move))
    return track


def FindPic(bg_image='./images/bgImages.png', block_image='./images/blockImages.png'):
    """

    :param bg_image:
    :param block_image:
    :return:
    """
    # 读取图片
    bg_rgb = cv2.imread(bg_image)
    # 灰度处理
    bg_gray = cv2.cvtColor(bg_rgb, cv2.COLOR_BGR2GRAY)
    # 读取滑块图片
    block_rgb = cv2.imread(block_image, 0)
    # 匹配滑块位置
    res = cv2.matchTemplate(bg_gray, block_rgb, cv2.TM_CCOEFF_NORMED)
    # 获取最佳匹配与最差匹配
    value = cv2.minMaxLoc(res)
    print(value)
    # 返回最佳匹配的X坐标
    return value[2][0]


driver = webdriver.Chrome('D:\DataCenter\PycharmProjects\my_tools\conf\chromedriver.exe')
driver.maximize_window()
driver.implicitly_wait(10)

driver.get('https://i.qq.com/')

driver.switch_to.frame('login_frame')

driver.find_element_by_xpath('//*[@id="switcher_plogin"]').click()

driver.find_element_by_xpath('//*[@id="u"]').send_keys('264675689')
driver.find_element_by_xpath('//*[@id="p"]').send_keys('kh168375313')

driver.find_element_by_xpath('//*[@id="login_button"]').click()

driver.switch_to.frame('tcaptcha_iframe')

slideBg = driver.find_element_by_xpath('//*[@id="slideBg"]')
slideBlock = driver.find_element_by_xpath('//*[@id="slideBlock"]')
slideBg_url = slideBg.get_attribute('src')
slideBlock_url = slideBlock.get_attribute('src')

print(slideBg_url)
bg_image = requests.get(slideBg_url).content
with open('./images/bgImages.png', 'wb') as f:
    f.write(bg_image)

block_image = requests.get(slideBlock_url).content
with open('./images/blockImages.png', 'wb') as f:
    f.write(block_image)


def get_offset(image, source_img, x):
    # print("我是x",x)
    # 根据自己电脑的实际情况调整
    for i in range(827, 1075):#遍历的是验证码的横坐标
        for j in range(420, 567):#遍历的是验证码的纵坐标
            pixel1 = image.getpixel((i, j))
            pixel2 = source_img.getpixel((i, j))
            if abs(pixel1[0]-pixel2[0]) >= 33 and abs(pixel1[1]-pixel2[1]) >= 33 and abs(pixel1[2]-pixel2[2]) >= 33:
                print("这是横坐标", i)
                print("这是纵坐标", j)
                print("这是pixel1", pixel1)
                print("这是pixel2", pixel2)
                # 获取到缺口偏移量
                print("这是缺口的左侧横坐标",i)       # 打印查看缺口x轴的偏移量
                print(i - 600 - x  - 13)
                return int(i - 600 - x  - 13)


# x = FindPic()
# print(x)
#
bg_image_l = cv2.imread('./images/bgImages.png')
# 背景图本地宽度
local_bg_image_width = bg_image_l.shape[1]
print(local_bg_image_width)
# 背景图网页宽度
page_bg_image_width = slideBg.size
print(page_bg_image_width)

# x = x * page_bg_image_width / local_bg_image_width

sleep(1)
driver.close()
