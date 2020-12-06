import random
import time
import cv2
import requests
import os

from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from functools import reduce

from .config import *


class Slider(object):
    def __init__(self, driver, window_proportion=1):
        self.driver = driver
        self.window_proportion = window_proportion

    def _get_elm_by_xpath(self, xpath):
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

    def get_offset(self, bg_image_info, block_image_info, block_border_offset, init_offset):
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
        # print(value)
        # 返回最佳匹配的X坐标
        # return value[2][0]
        x = value[2][0]
        # 网页与本地图片比例
        bg_image_proportion = bg_image_info.get('width') / bg_rgb.shape[1]
        block_image_proportion = block_image_info.get('width') / block_rgb.shape[1]
        x = x * bg_image_proportion + block_border_offset * block_image_proportion - init_offset / self.window_proportion
        return int(x)

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

    def run(self, site_type):

        reload_xpath = SLIDE_CODE.get(site_type).get('reload_xpath')
        bg_path = SLIDE_CODE.get(site_type).get('bg_image_xpath')
        block_path = SLIDE_CODE.get(site_type).get('block_image_xpath')
        slider_path = SLIDE_CODE.get(site_type).get('slider_xpath')
        success_check_xpath = SLIDE_CODE.get(site_type).get('success_check_xpath')
        block_border_offset = SLIDE_CODE.get(site_type).get('block_border_offset')
        init_offset = SLIDE_CODE.get(site_type).get('init_offset')

        i = 0
        while i < 10:
            try:
                self._get_elm_by_xpath(slider_path)
                i += 1
            except Exception as e:
                print('Verified')
                break

            # 点击刷新验证码
            self._get_elm_by_xpath(reload_xpath).click()
            # 获取图片
            # 背景图
            bg_image_info = self.get_image(bg_path, '%s/images/bgImages.png' % os.getcwd())
            # 滑块图
            block_image_info = self.get_image(block_path, '%s/images/blockImages.png' % os.getcwd())

            # 获取偏移量
            real_offset = self.get_offset(bg_image_info, block_image_info, block_border_offset, init_offset)
            print("The calculated offset: %s" % real_offset)

            # 获取滑动轨迹
            track = self.get_track(real_offset)

            move_offset = reduce(lambda x, y: x + y, track)
            print("The actually executed offset: %s" % move_offset)

            # 执行滑动
            self.move_to_gap(slider_path, track)
