from flask import request, Blueprint, render_template, jsonify, session
from flask_restful import Api, Resource
from models.graphs import *
from common.util import *
from common.draw_graph import *
from config import IMG_MAPPING, TEMP_GRAPH_BASE_IMG_PATH, TEMP_GRAPH_BASE_PAGE_PATH
from .cache import *


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
        graph_update_by_id(id, status=0)
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
    nodes = request.form.get('nodes')
    links = request.form.get('links')
    img_b64code = request.form.get('img_b64code')
    name = request.form.get('name')

    graph = graph_get_by_userid_and_nodes_and_inks(user_id, nodes, links)
    if not graph:
        try:
            graph_add(user_id, nodes, links, img_b64code, name)
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

@graphs.route('/graphs/draw', methods=['GET'])
def draw():
    def add_node_attr(nodes):
        for node in nodes:
            node['symbol'] = 'image://%s' % IMG_MAPPING.get(node['type']).get('b64code')
            node['symbolSize'] = 50
            # node['value'] = ['0.0.0.0']
            node['is_fixed'] = True
            # if node['name'] == 'Core router':
            #     node['x'] = 50
            #     node['y'] = 50
        return nodes

    nodes = redis.hget('nodes', '5fd0a07d3f1a9abb4c741b2f')
    links = redis.hget('links', '5fd0a07d3f1a9abb4c741b2f')
    if nodes and links:
        nodes = json.loads(nodes)
        links = json.loads(links)
    else:
        nodes = []
        links = []
    nodes = add_node_attr(nodes)

    filename = get_current_time_str() + get_random_str()
    fp = os.path.join(TEMP_GRAPH_BASE_IMG_PATH, filename + '.png')
    page = os.path.join(TEMP_GRAPH_BASE_PAGE_PATH, filename + '.html')

    dg = DrawGraph()
    dg.setting(title='网络拓扑图', line_width=2).exec_draw(nodes, links).save_img(fp, page)
    b64code = get_b64code(fp)

    # os.remove(page)
    # os.remove(fp)

    return jsonify(
        {
            'status': 0,
            'message': 'SUCCESS',
            'data': {
                'filename': filename + '.png',
                'b64code': b64code
            }
        }
    )
