from mongoengine import *
from datetime import datetime
from .users import Users
from bson import json_util


class CustomQuerySet(QuerySet):
    def to_json(self):
        return "[%s]" % (",".join([doc.to_json() for doc in self]))


class Links(Document):  # 继承document,类名为集合名,与数据库中集合名字相同,不分大小写
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


def link_add(user_id, source_node_id, target_node_id, describe, rome_port_id1, rome_port_id2):
    now = datetime.now()
    link = Links(user=Users.objects.get(id=user_id),
                 source_node_id=source_node_id,
                 target_node_id=target_node_id,
                 describe=describe,
                 rome_port_id1=rome_port_id1,
                 rome_port_id2=rome_port_id2,
                 create_time=now,
                 update_time=now,
                 status=1)
    link.save()
    return link


def link_get_by_id(id):
    link = Links.objects.filter(id=id).first()
    return link


def link_update_by_id(id, **kwargs):
    link = Links.objects.filter(id=id).first()
    link.update(**kwargs)
    return link


def link_delete_by_id(id):
    link = Links.objects.get(id=id)
    link.delete()
    return link


def link_get_by_userid_and_node_and_source_and_target(user_id, source, target):
    link = Links.objects.filter(user=Users.objects.get(id=user_id), source_node_id=source,
                                target_node_id=target).first()
    return link


def links_get_by_user_id(user_id):
    links = Links.objects(user__id=user_id).filter(status=1).all()
    return links


def get_all_links():
    links = Links.objects.all()
    return links
