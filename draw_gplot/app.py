# -*- coding: utf-8 -*-
# @Time    : 2020/12/8 20:40
# @Author  : keh123000
# @Email   : 26467568@qq.com
# @File    : app.py

from flask_restful import Api
from flask import Flask, render_template

app = Flask(__name__, static_folder='static', static_url_path='/static', template_folder='templates')


# def run():
#     dg = DrawGplot()
#     dg.setting(title='网络拓扑图demo', line_width=2).exec_draw(nodes, links).save_img()


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    api = Api(app)
    from views.user import User, users

    app.register_blueprint(users, url_prefix='')
    api.add_resource(User, '/user/<string:id>', endpoint='user')

    from views.node import Node, nodes

    app.register_blueprint(nodes, url_prefix='')
    api.add_resource(Node, '/node/<string:id>', endpoint='node')

    from views.link import Link, links

    app.register_blueprint(links, url_prefix='')
    api.add_resource(Link, '/link/<string:id>', endpoint='link')


    app.debug = True
    app.run(port=1680)
