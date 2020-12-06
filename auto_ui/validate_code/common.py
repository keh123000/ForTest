import cv2


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
