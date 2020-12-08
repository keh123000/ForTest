# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 19:49
# @Author  : keh123000
# @Email   : 26467568@qq.com
# @File    : manage.py.py

from app import create_app

app = create_app()

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=1680)
