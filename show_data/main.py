from show_data.util import *
from show_data.test_data import *
from show_data.forecharts import *

def run():
    dg = DrawGplot()
    dg.setting(title='网络拓扑图demo',line_width=2).exec_draw(nodes, links).save_img()


if __name__ == '__main__':
    run()
