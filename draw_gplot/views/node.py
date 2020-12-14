from flask import request, Blueprint, render_template, jsonify
from flask_restful import Api, Resource
from models.nodes import *
from models.users import *
from common.util import *
from .cache import *


class Node(Resource):
    def get(self, id):
        code = 1
        message = 'QUERY SUCCESS'
        data = node_get_by_id(id)
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
        node_update_by_id(id, code=0)
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
        node_update_by_id(id, code=0)
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
        # 更改节点状态做逻辑删除
        node_update_by_id(id, code=0)
        return jsonify(
            {
                'code': code,
                'message': message,
                'data': data
            }
        )


nodes = Blueprint('nodes', __name__)


@nodes.route('/node', methods=['POST'])
def add_node():
    code = 0
    message = 'FAIL'
    data = {}

    # req_data = request.get_data()
    user_id = request.form.get('user_id')
    name = request.form.get('name')
    describe = request.form.get('describe')
    type = request.form.get('type')
    slot_id = request.form.get('slot_id')
    port_id = request.form.get('port_id')
    remote_port_id = request.form.get('remote_port_id')

    node = node_get_by_user_id_and_node_name(user_id, name)
    if not node:
        try:
            node = node_add(user_id, name, describe, type, slot_id, port_id, remote_port_id)
            code = 1
            message = 'SUCCESS'
            node = convertMongoToDict(node)
            cache_add_graph_data('nodes', node, user_id)
        except Exception as e:
            node = None
            print(e)
    else:
        code = 2
        message = 'Already Exist'
        node = convertMongoToDict(node)
    if node:
        data = {
            'create_time': node.get('create_time'),
            'node_id': node.get('_id')

        }

    return jsonify(
        {
            'code': code,
            'message': message,
            'data': data
        }
    )


@nodes.route('/nodes/<string:user_id>', methods=['GET'])
def get_nodes_by_user_id(user_id):
    data = nodes_get_by_user_id(user_id)
    data = convertMongoToDict(list(data))
    cache_add_graph_data('nodes', data, user_id)
    return jsonify({
        'code': 1,
        'message': 'SUCCESS',
        'data': data
    })


@nodes.route('/nodes', methods=['GET'])
def get_nodes():
    data = get_all_nodes()
    data = convertMongoToDict(list(data))
    return jsonify({
        'code': 1,
        'message': 'SUCCESS',
        'data': data
    })
