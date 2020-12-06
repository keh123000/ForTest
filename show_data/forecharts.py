from pyecharts import options as opts
from pyecharts.charts import Graph
from pyecharts.render import make_snapshot
from snapshot_selenium import snapshot
from pyecharts.options.global_options import ThemeType


class DrawGplot(object):
    def __init__(self, width="1200px", height="800px"):
        self.graph = Graph(
            init_opts=opts.InitOpts(
                width=width,
                height=height,
                bg_color='rgba(255,255,255)'
            )
        )
        self.line_width = 1

    def __del__(self):
        pass


    def _default_setting(self):
        self.graph.set_global_opts()

    def setting(self, title=None, line_width: int = None):
        if title:
            self.graph.set_global_opts(title_opts=opts.TitleOpts(title=title), )
        if line_width:
            self.line_width = line_width
        return self

    def exec_draw(self, nodes, links):
        self.graph.add('',
                       nodes,
                       links,
                       repulsion=1000,
                       is_draggable=True,  # 节点是否可拖拽，只在使用力引导布局的时候有用。
                       linestyle_opts=opts.LineStyleOpts(width=self.line_width),
                       )
        return self

    def save_img(self, fp=None):
        if fp is None:
            fp = 'result.png'
        make_snapshot(snapshot, self.graph.render(), fp)
