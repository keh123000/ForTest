from flask import request, Blueprint, render_template, jsonify
from flask_restful import Api, Resource
from models.graphs import *
from common.util import *


class Graph(Resource):
    def get(self, id):
        status = 1
        message = 'QUERY SUCCESS'
        data = graph_get_by_id(id)
        data = convertMongoToDict(data)
        return jsonify(
            {
                'status': status,
                'message': message,
                'data': data
            }
        )

    def put(self, id):
        status = 1
        message = 'UPDATE SUCCESS'
        data = {}
        graph_update_by_id(id, status=0)
        return jsonify(
            {
                'status': status,
                'message': message,
                'data': data
            }
        )

    def patch(self, id):
        status = 1
        message = 'UPDATE SUCCESS'
        data = {}
        graph_update_by_id(id, status=0)
        return jsonify(
            {
                'status': status,
                'message': message,
                'data': data
            }
        )

    def delete(self, id):
        status = 1
        message = 'DELETE SUCCESS'
        data = {}
        # 更改节点状态做逻辑删除
        graph_update_by_id(id,status=0)
        return jsonify(
            {
                'status': status,
                'message': message,
                'data': data
            }
        )


graphs = Blueprint('graphs', __name__)


@graphs.route('/graph', methods=['POST'])
def add_graph():
    status = 0
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

    graph = graph_get_by_user_id_and_graph_name(user_id, name)
    if not graph:
        try:
            graph_add(user_id, name, describe, type, slot_id, port_id, remote_port_id)
            status = 1
            message = 'SUCCESS'
        except Exception as e:
            print(e)
    else:
        graph = convertMongoToDict(graph)
        status = 2
        message = 'Already Exist'
        data = {
            'create_time': graph.get('create_time'),
            'graph_id': graph.get('_id')

        }

    return jsonify(
        {
            'status': status,
            'message': message,
            'data': data
        }
    )


@graphs.route('/graphs/<string:user_id>', methods=['GET'])
def get_graphs_by_user_id(user_id):
    data = graphs_get_by_user_id(user_id)
    data = convertMongoToDict(list(data))
    return {
        'status': 0,
        'message': 'SUCCESS',
        'data': data
    }


@graphs.route('/graphs', methods=['GET'])
def get_graphs():
    data = get_all_graphs()
    data = convertMongoToDict(list(data))
    return {
        'status': 0,
        'message': 'SUCCESS',
        'data': data
    }
