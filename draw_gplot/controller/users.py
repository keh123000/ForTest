from flask import request,Blueprint, render_template
from models.users import *

users = Blueprint('users', __name__)


@users.route('/users', methods=['POST'])
def add_user():
    data = request.get_data()
    username = request.form.get('username')
    password = request.form.get('password')
    user_add(username, password)
    return '新增用户'
