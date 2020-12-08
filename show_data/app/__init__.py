# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 19:43
# @Author  : keh123000
# @Email   : 26467568@qq.com
# @File    : __init__.py.py


from flask import Flask
from ..config import DevConfig


def create_app():
    app = Flask(__name__)
    app.config.from_object(DevConfig)
    app.config['JSON_AS_ASCII'] = False  # 这个配置可以确保http请求返回的json数据中正常显示中文
    return app
