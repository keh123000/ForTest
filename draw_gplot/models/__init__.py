# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 19:52
# @Author  : keh123000
# @Email   : 26467568@qq.com
# @File    : __init__.py.py

from mongoengine import *

host ='192.168.0.178'
port = 27017
user = 'test'
password = '123456'
db_name = 'test'
collection = 'test'
db_url = 'mongodb://test:123456@192.168.1.178:27017/test'

a = connect(db=db_name, host=host, port=port, username=user, password=password)
# connect(db_name, host=db_url)
