from flask import Flask,render_template

from show_data.util import *
from show_data.test_data import *
from show_data.forecharts import *

app = Flask(__name__, static_folder='static', static_url_path='/static',template_folder='templates')


def run():
    dg = DrawGplot()
    dg.setting(title='网络拓扑图demo', line_width=2).exec_draw(nodes, links).save_img()


@app.route('/')
def hello_world():
    return render_template('index.html')


if __name__ == '__main__':
    app.debug = True
    app.run(port=1680)
