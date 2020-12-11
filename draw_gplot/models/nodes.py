from mongoengine import *
from datetime import datetime

from .users import Users


class Nodes(Document):  # 继承document,类名为集合名,与数据库中集合名字相同,不分大小写
    # user = ReferenceField(Users)
    user_id = StringField(required=True)
    name = StringField(required=True)
    describe = StringField()
    type = StringField()
    slot_id = StringField(required=True)
    port_id = StringField(required=True)
    remote_port_id = StringField(required=True)
    create_time = DateTimeField()
    update_time = DateTimeField(required=True,default=datetime.now())
    status = IntField(required=True, default=1)


def node_add(user_id, name, describe, type, slot_id, port_id, remote_port_id):
    now = datetime.now()
    node = Nodes(user_id=user_id,
                 name=name,
                 describe=describe,
                 type=type,
                 slot_id=slot_id,
                 port_id=port_id,
                 remote_port_id=remote_port_id,
                 create_time=now,
                 update_time=now)
    node.save()
    return node


def node_get_by_id(id):
    node = Nodes.objects.filter(id=id).first()
    return node


def node_update_by_id(id, **kwargs):
    node = Nodes.objects.filter(id=id).first()
    node.update(**kwargs)
    return node


def node_delete_by_id(id):
    node = Nodes.objects.get(id=id)
    node.delete()
    return node


def node_get_by_user_id_and_node_name(user_id, name):
    node = Nodes.objects.filter(user_id=user_id, name=name).first()
    return node


def nodes_get_by_user_id(user_id):
    nodes = Nodes.objects.filter(user_id=user_id, status=1).order_by('update_time').all()
    return nodes


def get_all_nodes():
    nodes = Nodes.objects.all()
    return nodes
