from mongoengine import *
from datetime import datetime


class Users(Document):  # 继承document,类名为集合名,与数据库中集合名字相同,不分大小写
    username = StringField()
    password = StringField()
    create_time = DateTimeField()
    update_time = DateTimeField()
    status = IntField()


def user_add(username, password):
    now = datetime.now()
    user = Users(username=username, password=password, create_time=now, update_time=now, status=1)
    user.save()
    return user


def get_user_by_name(username):
    user = Users.objects.filter(username=username).first()

    return user


def get_all_users():
    users = Users.objects.all()
    print(users)
    from common.doc2json import convertMongoToJson
    users = convertMongoToJson(users)
    print(users)
    return users
