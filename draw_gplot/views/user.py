# -*- coding: utf-8 -*-
# @Time    : 2020/12/9 20:14
# @Author  : keh123000
# @Email   : 26467568@qq.com
# @File    : user.py

from flask import request, Blueprint, render_template, jsonify
from flask_restful import Api, Resource
from models.users import *
from common.util import *


class User(Resource):
    def get(self, id):
        return '查询指定用户信息'

    def put(self, id):
        return '全量更新用户信息'

    def patch(self, id):
        return '局部更新用户信息'

    def delete(self, id):
        return '删除指定用户信息'


users = Blueprint('users', __name__)


@users.route('/user', methods=['POST'])
def add_user():
    status = 0
    message = '注册失败'
    data = {}

    # req_data = request.get_data()
    username = request.form.get('username')
    password = request.form.get('password')

    user = user_get_by_name(username)
    if not user:
        try:
            user_add(username, password)
            status = 1
            message = '注册成功'
        except Exception as e:
            print(e)
    else:
        status = 2
        message = '已注册'
        data = {
            'create_time': user.get('create_time')
        }

    return jsonify(
        {
            'status': status,
            'message': message,
            'data': data
        }
    )


@users.route('/users', methods=['GET'])
def get_users():
    users = get_all_users()
    users = convertMongoToDict(list(users))
    return {
        'status': 0,
        'message': 'SUCCESS',
        'data': users
    }
