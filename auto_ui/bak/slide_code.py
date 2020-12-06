# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 10:56
# @Author  : keh123000
# @Email   : 26467568@qq.com
# @File    : slide_code.py
# -*-coding:utf-8 -*-
import random
import time

from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from urllib.request import urlretrieve
from selenium import webdriver
from bs4 import BeautifulSoup
import PIL.Image as image
import re
import cv2
import requests
import os


class Slider(object):
    def __init__(self, driver,
                 window_proportion=1
                 ):
        self.driver = driver
        self.window_proportion = window_proportion

    def _get_elm_by_xpath(self, xpath):
        print(xpath)
        return WebDriverWait(self.driver, 20, 0.5).until(lambda x: x.find_element_by_xpath(xpath))

    def get_image(self, xpath, fp):
        image_info = {"file_name": fp}
        # 获取页面图片元素信息
        image_elm = self._get_elm_by_xpath(xpath)
        # 获取图片宽高
        image_info.update(image_elm.size)
        # 下载图片至本地
        image = requests.get(image_elm.get_attribute('src')).content
        with open(fp, 'wb') as f:
            f.write(image)
        return image_info

    def match_image(self, bg_image='./images/bgImages.png', block_image='./images/blockImages.png'):
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

    def get_offset(self, bg_image_info, block_image_info, left_border_offset, init_offset):
        # 读取图片
        bg_rgb = cv2.imread(bg_image_info.get('file_name'))
        # 灰度处理
        bg_gray = cv2.cvtColor(bg_rgb, cv2.COLOR_BGR2GRAY)
        # 读取滑块图片
        block_rgb = cv2.imread(block_image_info.get('file_name'), 0)
        # 匹配滑块位置
        res = cv2.matchTemplate(bg_gray, block_rgb, cv2.TM_CCOEFF_NORMED)
        # 获取最佳匹配与最差匹配
        value = cv2.minMaxLoc(res)
        print(value)
        # 返回最佳匹配的X坐标
        # return value[2][0]
        x = value[2][0]
        # 网页与本地图片比例
        bg_image_proportion = bg_image_info.get('width') / bg_rgb.shape[1]
        block_image_proportion = block_image_info.get('width') / block_rgb.shape[1]
        x = x * bg_image_proportion + left_border_offset * block_image_proportion - init_offset / self.window_proportion
        print("偏移量：%s" % x)
        return int(x)

    # # 滑块移动轨迹
    # def get_track(self, distance):
    #     track = []
    #     current = 0
    #     mid = distance * 3 / 4
    #     t = random.uniform(0.2, 0.4)
    #     v = 0
    #     while current < distance:
    #         if current < mid:
    #             a = 2
    #         else:
    #             a = -3
    #         v0 = v
    #         v = v0 + a * t
    #         move = v0 * t + 1 / 2 * a * t * t
    #         current += move
    #         track.append(round(move))
    #     return track

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 3 / 4
        # 计算间隔
        t = random.uniform(0.2, 0.4)
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def move_to_gap(self, slider_xpth, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        slider = self._get_elm_by_xpath(slider_xpth)
        ActionChains(self.driver).click_and_hold(slider).perform()
        while track:
            x = random.choice(track)
            ActionChains(self.driver).move_by_offset(xoffset=x, yoffset=0).perform()
            track.remove(x)
        time.sleep(0.5)
        ActionChains(self.driver).release().perform()

    def run(self, bg_path,
            block_path,
            slider_path,
            left_border_offset=0):
        # 获取图片
        # 背景图
        bg_image_info = self.get_image(bg_path, '%s/images/bgImages.png' % os.getcwd())
        # 滑块图
        block_image_info = self.get_image(block_path, '%s/images/blockImages.png' % os.getcwd())

        # # 获取初始匹配偏移量
        # x = self.match_image(bg_image_info.get('file_name'), block_image_info.get('file_name'))
        # 获取相对准确偏移量
        x = self.get_offset(bg_image_info, block_image_info, 24, 48)

        # 获取滑动轨迹
        track = self.get_track(x)
        print(track)

        from functools import reduce
        print(reduce(lambda x, y: x + y, track))

        # 执行滑动
        self.move_to_gap(slider_path, track)


# 获取背景及滑块图片


class Crack():
    def __init__(self, username, passwd):
        self.url = 'https://passport.bilibili.com/login'
        self.browser = webdriver.Chrome('D:\DataCenter\PycharmProjects\my_tools\conf\chromedriver.exe')
        self.wait = WebDriverWait(self.browser, 100)
        self.BORDER = 6
        self.passwd = passwd
        self.username = username

    def open(self):
        """
        打开浏览器,并输入查询内容
        """
        self.browser.get(self.url)
        keyword = self.wait.until(EC.presence_of_element_located((By.ID, 'login-username')))
        keyword.send_keys('')
        keyword = self.wait.until(EC.presence_of_element_located((By.ID, 'login-passwd')))
        keyword.send_keys('')
        # bowton.click()

    def get_images(self, bg_filename='bg.jpg', fullbg_filename='fullbg.jpg'):
        """
        获取验证码图片
        :return: 图片的location信息
        """
        bg = []
        fullgb = []
        while bg == [] and fullgb == []:
            bf = BeautifulSoup(self.browser.page_source, 'lxml')
            bg = bf.find_all('div', class_='gt_cut_bg_slice')
            fullgb = bf.find_all('div', class_='gt_cut_fullbg_slice')
        bg_url = re.findall('url\(\"(.*)\"\);', bg[0].get('style'))[0].replace('webp', 'jpg')
        fullgb_url = re.findall('url\(\"(.*)\"\);', fullgb[0].get('style'))[0].replace('webp', 'jpg')
        bg_location_list = []
        fullbg_location_list = []
        for each_bg in bg:
            location = {}
            location['x'] = int(re.findall('background-position: (.*)px (.*)px;', each_bg.get('style'))[0][0])
            location['y'] = int(re.findall('background-position: (.*)px (.*)px;', each_bg.get('style'))[0][1])
            bg_location_list.append(location)
        for each_fullgb in fullgb:
            location = {}
            location['x'] = int(re.findall('background-position: (.*)px (.*)px;', each_fullgb.get('style'))[0][0])
            location['y'] = int(re.findall('background-position: (.*)px (.*)px;', each_fullgb.get('style'))[0][1])
            fullbg_location_list.append(location)

        urlretrieve(url=bg_url, filename=bg_filename)
        print('缺口图片下载完成')
        urlretrieve(url=fullgb_url, filename=fullbg_filename)
        print('背景图片下载完成')
        return bg_location_list, fullbg_location_list

    def get_merge_image(self, filename, location_list):
        """
        根据位置对图片进行合并还原
        :filename:图片
        :location_list:图片位置
        """
        im = image.open(filename)
        new_im = image.new('RGB', (260, 116))
        im_list_upper = []
        im_list_down = []

        for location in location_list:
            if location['y'] == -58:
                im_list_upper.append(im.crop((abs(location['x']), 58, abs(location['x']) + 10, 166)))
            if location['y'] == 0:
                im_list_down.append(im.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

        new_im = image.new('RGB', (260, 116))

        x_offset = 0
        for im in im_list_upper:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]

        x_offset = 0
        for im in im_list_down:
            new_im.paste(im, (x_offset, 58))
            x_offset += im.size[0]

        new_im.save(filename)

        return new_im

    def get_merge_image(self, filename, location_list):
        """
        根据位置对图片进行合并还原
        :filename:图片
        :location_list:图片位置
        """
        im = image.open(filename)
        new_im = image.new('RGB', (260, 116))
        im_list_upper = []
        im_list_down = []

        for location in location_list:
            if location['y'] == -58:
                im_list_upper.append(im.crop((abs(location['x']), 58, abs(location['x']) + 10, 166)))
            if location['y'] == 0:
                im_list_down.append(im.crop((abs(location['x']), 0, abs(location['x']) + 10, 58)))

        new_im = image.new('RGB', (260, 116))

        x_offset = 0
        for im in im_list_upper:
            new_im.paste(im, (x_offset, 0))
            x_offset += im.size[0]

        x_offset = 0
        for im in im_list_down:
            new_im.paste(im, (x_offset, 58))
            x_offset += im.size[0]

        new_im.save(filename)

        return new_im

    def is_pixel_equal(self, img1, img2, x, y):
        """
        判断两个像素是否相同
        :param image1: 图片1
        :param image2: 图片2
        :param x: 位置x
        :param y: 位置y
        :return: 像素是否相同
        """
        # 取两个图片的像素点
        pix1 = img1.load()[x, y]
        pix2 = img2.load()[x, y]
        threshold = 60
        if (abs(pix1[0] - pix2[0] < threshold) and abs(pix1[1] - pix2[1] < threshold) and abs(
                pix1[2] - pix2[2] < threshold)):
            return True
        else:
            return False

    def get_gap(self, img1, img2):
        """
        获取缺口偏移量
        :param img1: 不带缺口图片
        :param img2: 带缺口图片
        :return:
        """
        left = 43
        for i in range(left, img1.size[0]):
            for j in range(img1.size[1]):
                if not self.is_pixel_equal(img1, img2, i, j):
                    left = i
                    return left
        return left

    def get_track(self, distance):
        """
        根据偏移量获取移动轨迹
        :param distance: 偏移量
        :return: 移动轨迹
        """
        # 移动轨迹
        track = []
        # 当前位移
        current = 0
        # 减速阈值
        mid = distance * 4 / 5
        # 计算间隔
        t = 0.2
        # 初速度
        v = 0

        while current < distance:
            if current < mid:
                # 加速度为正2
                a = 2
            else:
                # 加速度为负3
                a = -3
            # 初速度v0
            v0 = v
            # 当前速度v = v0 + at
            v = v0 + a * t
            # 移动距离x = v0t + 1/2 * a * t^2
            move = v0 * t + 1 / 2 * a * t * t
            # 当前位移
            current += move
            # 加入轨迹
            track.append(round(move))
        return track

    def get_slider(self):
        """
        获取滑块
        :return: 滑块对象
        """
        while True:
            try:
                slider = self.browser.find_element_by_xpath("//div[@class='gt_slider_knob gt_show']")
                break
            except:
                time.sleep(0.5)
        return slider

    def move_to_gap(self, slider, track):
        """
        拖动滑块到缺口处
        :param slider: 滑块
        :param track: 轨迹
        :return:
        """
        ActionChains(self.browser).click_and_hold(slider).perform()
        while track:
            x = random.choice(track)
            ActionChains(self.browser).move_by_offset(xoffset=x, yoffset=0).perform()
            track.remove(x)
        time.sleep(0.5)
        ActionChains(self.browser).release().perform()

    def crack(self):
        # 打开浏览器
        self.open()

        # 保存的图片名字
        bg_filename = 'bg.jpg'
        fullbg_filename = 'fullbg.jpg'

        # 获取图片
        bg_location_list, fullbg_location_list = self.get_images(bg_filename, fullbg_filename)

        # 根据位置对图片进行合并还原
        bg_img = self.get_merge_image(bg_filename, bg_location_list)
        fullbg_img = self.get_merge_image(fullbg_filename, fullbg_location_list)

        # 获取缺口位置
        gap = self.get_gap(fullbg_img, bg_img)
        print('缺口位置', gap)

        track = self.get_track(gap - self.BORDER)
        print('滑动滑块')
        print(track)

        # 点按呼出缺口
        slider = self.get_slider()
        # 拖动滑块到缺口处
        self.move_to_gap(slider, track)

# if __name__ == '__main__':
# crack = Crack('username', 'passwd')
# crack.crack()
# print('验证成功')
