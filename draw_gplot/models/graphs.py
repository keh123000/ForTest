from mongoengine import *
from datetime import datetime
from .users import Users
from bson import json_util


class CustomQuerySet(QuerySet):
    def to_json(self):
        return "[%s]" % (",".join([doc.to_json() for doc in self]))


class Graphs(Document):  # 继承document,类名为集合名,与数据库中集合名字相同,不分大小写
    # user = ReferenceField(Users)
    user_id = StringField(required=True)
    nodes = ListField(StringField(), required=True, default=[])
    links = ListField(StringField(), required=True, default=[])
    img_b64code = StringField(required=True)
    name = StringField(required=True)
    create_time = DateTimeField()
    update_time = DateTimeField(required=True, default=datetime.now())
    status = IntField(required=True)


def graph_add(user_id, nodes, links, img_b64code, name):
    now = datetime.now()
    graph = Graphs(user_id=user_id,
                   nodes=nodes,
                   links=links,
                   img_b64code=img_b64code,
                   name=name,
                   create_time=now,
                   update_time=now,
                   status=1)
    graph.save()
    return graph


def graph_get_by_id(id):
    graph = Graphs.objects.filter(id=id).first()
    return graph


def graph_update_by_id(id, **kwargs):
    now = datetime.now()
    graph = Graphs.objects.filter(id=id).first()
    graph.update(update_time=now, **kwargs)
    return graph


def graph_delete_by_id(id):
    graph = Graphs.objects.get(id=id)
    graph.delete()
    return graph


def graph_get_by_userid_and_nodes_and_inks(user_id, nodes, links):
    graph = Graphs.objects.filter(user_id=user_id, nodes=nodes, links=links).first()
    return graph


def graphs_get_by_user_id(user_id):
    graphs = Graphs.objects(user_id=user_id).filter(status=1).all()
    return graphs


def get_all_graphs():
    graphs = Graphs.objects.all()
    return graphs
