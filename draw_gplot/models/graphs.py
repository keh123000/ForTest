from mongoengine import *
from datetime import datetime
from .users import Users
from bson import json_util


class CustomQuerySet(QuerySet):
    def to_json(self):
        return "[%s]" % (",".join([doc.to_json() for doc in self]))


class Graphs(Document):  # 继承document,类名为集合名,与数据库中集合名字相同,不分大小写
    user = ReferenceField(Users)
    # user_id = StringField(required=True)
    source_node_id = StringField(required=True)
    target_node_id = StringField(required=True)
    describe = StringField()
    rome_port_id1 = StringField(required=True)
    rome_port_id2 = StringField(required=True)
    create_time = DateTimeField(required=True)
    update_time = DateTimeField(required=True)
    status = IntField(required=True)

    meta = {'queryset_class': CustomQuerySet}

    def to_json(self):
        data = self.to_mongo()
        data["user"] = {"User": {"username": self.user.username}}
        return json_util.dumps(data)


def graph_add(user_id, source_node_id, target_node_id, describe, rome_port_id1, rome_port_id2):
    now = datetime.now()
    graph = Graphs(user=Users.objects.get(id=user_id),
                 source_node_id=source_node_id,
                 target_node_id=target_node_id,
                 describe=describe,
                 rome_port_id1=rome_port_id1,
                 rome_port_id2=rome_port_id2,
                 create_time=now,
                 update_time=now,
                 status=1)
    graph.save()
    return graph


def graph_get_by_id(id):
    graph = Graphs.objects.filter(id=id).first()
    return graph


def graph_update_by_id(id, **kwargs):
    graph = Graphs.objects.filter(id=id).first()
    graph.update(**kwargs)
    return graph


def graph_delete_by_id(id):
    graph = Graphs.objects.get(id=id)
    graph.delete()
    return graph


def graph_get_by_userid_and_node_and_source_and_target(user_id, source, target):
    graph = Graphs.objects.filter(user=Users.objects.get(id=user_id), source_node_id=source,
                                target_node_id=target).first()
    return graph


def graphs_get_by_user_id(user_id):
    graphs = Graphs.objects(user__id=user_id).filter(status=1).all()
    return graphs


def get_all_graphs():
    graphs = Graphs.objects.all()
    return graphs
