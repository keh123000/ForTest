# -*- coding: utf-8 -*-
# @Time    : 2020/11/24 14:34
# @Author  : keh123000
# @Email   : 26467568@qq.com
# @File    : utils.py
import random
import string
from datetime import datetime


def get_current_time_str(fmt="%Y%m%d%H%M%S%f"):
    return datetime.now().strftime(fmt)


def get_random_str(length=5):
    return ''.join(random.sample(string.ascii_letters + string.digits, length))
