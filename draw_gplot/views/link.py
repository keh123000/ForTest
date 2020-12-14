from flask import request, Blueprint, render_template, jsonify
from flask_restful import Api, Resource
from models.links import *
from models.users import *
from common.util import *
from .cache import *


class Link(Resource):
    def get(self, id):
        code = 1
        message = 'QUERY SUCCESS'
        data = link_get_by_id(id)
        if data:
            user_data = user_get_by_id(data.user_id)
            user_data = convertMongoToDict(user_data)
            data = convertMongoToDict(data)
            if 'user_id' in data.keys():
                data.pop('user_id')
                data['user'] = user_data
        return jsonify(
            {
                'code': code,
                'message': message,
                'data': data
            }
        )

    def put(self, id):
        code = 1
        message = 'UPDATE SUCCESS'
        data = {}
        link_update_by_id(id, code=0)
        return jsonify(
            {
                'code': code,
                'message': message,
                'data': data
            }
        )

    def patch(self, id):
        code = 1
        message = 'UPDATE SUCCESS'
        data = {}
        link_update_by_id(id, code=0)
        return jsonify(
            {
                'code': code,
                'message': message,
                'data': data
            }
        )

    def delete(self, id):
        code = 1
        message = 'DELETE SUCCESS'
        data = {}
        # 更改连线状态做逻辑删除
        link_update_by_id(id, code=0)
        return jsonify(
            {
                'code': code,
                'message': message,
                'data': data
            }
        )


links = Blueprint('links', __name__)


@links.route('/link', methods=['POST'])
def add_link():
    code = 0
    message = 'FAIL'
    data = {}

    # req_data = request.get_data()
    user_id = request.form.get('user_id')
    source_node_id = request.form.get('source_node_id')
    target_node_id = request.form.get('target_node_id')
    describe = request.form.get('describe')
    rome_port_id1 = request.form.get('rome_port_id1')
    rome_port_id2 = request.form.get('rome_port_id2')

    link = link_get_by_userid_and_source_and_target(user_id, source_node_id, target_node_id)
    if not link:
        try:
            link = link_add(user_id, source_node_id, target_node_id, describe, rome_port_id1, rome_port_id2)
            code = 1
            message = 'SUCCESS'
            link = convertMongoToDict(link)
            cache_add_graph_data('links', link, user_id)
        except Exception as e:
            print(e)
    else:
        code = 2
        message = 'Already Exist'
        link = convertMongoToDict(link)
    if link:
        data = {
            'create_time': link.get('create_time'),
            'link_id': link.get('_id')

        }

    return jsonify(
        {
            'code': code,
            'message': message,
            'data': data
        }
    )


@links.route('/links/<string:user_id>', methods=['GET'])
def get_links_by_user_id(user_id):
    data = links_get_by_user_id(user_id)
    data = convertMongoToDict(list(data))
    cache_add_graph_data('links', data, user_id)
    return {
        'code': 1,
        'message': 'SUCCESS',
        'data': data
    }


@links.route('/links', methods=['GET'])
def get_links():
    data = get_all_links()
    data = convertMongoToDict(list(data))
    return {
        'code': 1,
        'message': 'SUCCESS',
        'data': data
    }
