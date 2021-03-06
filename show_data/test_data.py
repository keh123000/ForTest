string_value = '我是中国人，我爱我的祖国。'
int_value = 2048
init_list = [string_value, int_value, 'and']
init_dict = {
    'name': 'keh',
    'age': 26,
    'haja': "init_list",
    'indict': {'name': 'keh', 'age': 26, 'haja': ['我是中国人，我爱我的祖国。', 2048, 'and']}
}
list_value = [string_value, int_value, init_dict]

gplot_data = [
    {
        "id": "1",
        "name": "DC",
        "cn_name": "",
        "sub_node": "DC",
        "location": {
            "x": 150,
            "y": 222,
        },
        "size": {
            "width": 30,
            "height": 30
        }
    },
    {
        "id": "1",
        "name": "DC",
        "cn_name": "",
        "sub_node": "DC",
        "location": {
            "x": 150,
            "y": 222,
        },
        "size": {
            "width": 30,
            "height": 30
        }
    }
]
node_demo = {
    "id": "1",
    "name": "DC",
    "cn_name": "",
    "sub_node": "DC",
    "location": {
        "x": 150,
        "y": 222,
    },
    "size": {
        "width": 30,
        "height": 30
    }
}
node_list = ['AP', 'Core router', 'DC', 'Firewall', 'GK', 'HandSet', 'PSE', 'Splitter', 'Terminal', 'TV', 'WAP']

nodes = [
    {'type': "Core router", "name": "Core router"},
    {'type': "AP", "name": "AP"},
    {'type': "AP", "name": "AP2"},
    {'type': "DC", "name": "DC"},
    {'type': "Splitter", "name": "Splitter1"},
    {'type': "Splitter", "name": "Splitter2"},
    {'type': "Firewall", "name": "Firewall"},
    {'type': "Terminal", "name": "Terminal"},
    {'type': "Terminal", "name": "Terminal2"},
    {'type': "Terminal", "name": "Terminal3"},
    {'type': "TV", "name": "TV"},
]

links = [
    {"source": "Core router", "target": "DC", "name": ""},
    {"source": "Core router", "target": "AP", "name": ""},
    {"source": "Core router", "target": "AP2", "name": ""},
    {"source": "DC", "target": "Splitter1", "name": ""},
    {"source": "DC", "target": "Splitter2", "name": ""},
    {"source": "AP", "target": "TV", "name": ""},
    {"source": "AP2", "target": "Firewall", "name": ""},
    {"source": "Firewall", "target": "Terminal", "name": ""},
    {"source": "Firewall", "target": "Terminal2", "name": ""},
    {"source": "Firewall", "target": "Terminal3", "name": ""}

]

from show_data.config import *


def add_attr(nodes):
    for node in nodes:
        node['symbol'] = 'image://%s' % IMG_MAPPING.get(node['type']).get('b64code')
        node['symbolSize'] = 50
        node['value'] = ['0.0.0.0']
        node['is_fixed'] = True
        if node['name'] == 'Core router':
            node['x'] = 50
            node['y'] = 50
    return nodes


nodes = add_attr(nodes)
