# from PIL import Image
#
# img = Image.open("./validate_code/images/blockImages.png")  # 读取系统的内照片
#
# width = img.size[0]  # 长度
# height = img.size[1]  # 宽度
# temp = 1
# for i in range(0, width):  # 遍历所有长度的点
#     temp += 1
#     for j in range(0, height):  # 遍历所有宽度的点
#         if temp % 2 == 0:
#             img.putpixel((i, j), (255, 255, 255))
# img = img.convert("RGB")  # 把图片强制转成RGB
# img.save("4.png")  # 保存修改像素点后的图片
import cv2

#
# from PIL import Image
#
# im1 = Image.open("./validate_code/images/blockImages.png")
# print("im1的色彩模式为{}".format(im1.mode))

# 读取图片
# bg_rgb = cv2.imread("./validate_code/images/blockImages.png", cv2.IMREAD_UNCHANGED)
#
#
# print(bg_rgb.shape)
# b, g, r, al = cv2.split(bg_rgb)
# print(len(al))
# print(al[20])
#
# print(r[10][10])
# print(g[63][51])
# print(b[63][51])
#
# print(len(r))
# print(len(r[0]))
#
# print(r[50])
# print(g[50])
# print(b[50])


# from auto_ui.ui_engine import ui_operation
#
#
# uoe = ui_operation.UiOperation()
# uoe.run()

# import numpy as np
#
# print(type(np.random.randint(0,1)))


import os
import functools
import inspect


# from .logger import info, error


def get_secret_key(n: int = 16):
    """
    返回一个有n个byte那么长的一个string，用于加密。
    :param len: 期望返回字符串的byte长度
    :return: 随机生成的字符串
    """
    return os.urandom(n)


def get_current_function_name():
    """
    获取当前执行函数的函数名
    """
    return inspect.stack()[1][3]


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        try:
            print('call %s(): args = %s ,kwargs = %s' % (func.__name__, args, kwargs))
            return func(*args, **kwargs)
        except Exception as e:
            print("{0} is error,here are details:{1}".format(func.__name__,e))
            raise e

    return wrapper



def log_with_param(param):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            print('call %s():' % func.__name__)
            print('args = {}'.format(args))
            print('kwargs = {}'.format(kwargs))
            print('log_param = {}'.format(param))
            return func(*args, **kwargs)

        return wrapper

    return decorator


def func_error_log(param):
    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            try:
                return func(*args, **kwargs)
            except Exception as e:
                print(e)
                raise e

            # return func(*args, **kwargs)

        return wrapper

    return decorator


@log
def test1(num):
    a = num/0
    return a


def test2():
    test1(10)
    return 1

try:
    test2()
except Exception as e:
    print(e)
