from flask import request, Blueprint, render_template, jsonify, session
from flask_restful import Api, Resource
from models.graphs import *
from common.util import *
from common.draw_graph import *
from config import IMG_MAPPING, TEMP_GRAPH_BASE_IMG_PATH, TEMP_GRAPH_BASE_PAGE_PATH
from .cache import *


class Graph(Resource):
    def get(self, id):
        code = 1
        message = 'QUERY SUCCESS'
        data = graph_get_by_id(id)
        data = convertMongoToDict(data)
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
        graph_update_by_id(id, code=0)
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
        graph_update_by_id(id, code=0)
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
        graph_update_by_id(id, code=0)
        return jsonify(
            {
                'code': code,
                'message': message,
                'data': data
            }
        )


graphs = Blueprint('graphs', __name__)


@graphs.route('/graph', methods=['POST'])
def add_graph():
    code = 0
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
            code = 1
            message = 'SUCCESS'
        except Exception as e:
            print(e)
    else:
        graph = convertMongoToDict(graph)
        code = 2
        message = 'Already Exist'
        data = {
            'create_time': graph.get('create_time'),
            'graph_id': graph.get('_id')

        }

    return jsonify(
        {
            'code': code,
            'message': message,
            'data': data
        }
    )


@graphs.route('/graphs/<string:user_id>', methods=['GET'])
def get_graphs_by_user_id(user_id):
    data = graphs_get_by_user_id(user_id)
    data = convertMongoToDict(list(data))
    return {
        'code': 0,
        'message': 'SUCCESS',
        'data': data
    }


@graphs.route('/graphs', methods=['GET'])
def get_graphs():
    data = get_all_graphs()
    data = convertMongoToDict(list(data))
    return {
        'code': 0,
        'message': 'SUCCESS',
        'data': data
    }


@graphs.route('/graphs/draw', methods=['POST'])
def draw(user_id=None, title='网络拓扑图'):
    if not user_id:
        user_id = request.form.get('user_id')

    def get_nodes_and_links(user_id):
        nodes = []
        links = []
        nodes_list = redis.lrange('graph_nodes_%s' % user_id, 0, -1)
        links_list = redis.lrange('graph_links_%s' % user_id, 0, -1)

        temp_nodes = {}
        for node_id in nodes_list:
            node_dict = {
                'is_fixed': True,
                'symbolSize': 50
            }
            node = redis.hget('nodes', node_id)
            node = json.loads(node)
            name = node.get('name')
            types = node.get('type')
            node_dict['name'] = name
            node_dict['symbol'] = 'image://%s' % IMG_MAPPING.get(types).get('b64code')
            nodes.append(node_dict)

            temp_nodes[str(node_id, encoding='utf-8')] = name

        for link_id in links_list:
            link_dict = {}
            link = redis.hget('links', link_id)
            link = json.loads(link)
            link_dict['source'] = temp_nodes.get(link.get('source_node_id'))
            link_dict['target'] = temp_nodes.get(link.get('target_node_id'))
            links.append(link_dict)
        return nodes, links

    nodes, links = get_nodes_and_links(user_id)

    filename = get_current_time_str() + get_random_str()
    fp = os.path.join(TEMP_GRAPH_BASE_IMG_PATH, filename + '.png')
    page = os.path.join(TEMP_GRAPH_BASE_PAGE_PATH, filename + '.html')

    dg = DrawGraph()
    dg.setting(title=title, line_width=2).exec_draw(nodes, links).save_img(fp, page)
    b64code = get_b64code(fp)

    # os.remove(page)
    # os.remove(fp)

    return jsonify(
        {
            'code': 0,
            'message': 'SUCCESS',
            'data': {
                'filename': filename + '.png',
                'b64code': b64code
            }
        }
    )
