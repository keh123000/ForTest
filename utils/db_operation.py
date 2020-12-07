import redis
import pymongo
import pymysql
from pymysql.cursors import DictCursor
from elasticsearch import Elasticsearch
from elasticsearch import helpers

from utils.common import *


class MysqlDB(object):
    def __init__(self, host, port: int, user, password, db):
        self.conn = pymysql.connect(host=host, port=port, user=user, password=password, db=db, charset='utf8')
        self.cursor = self.conn.cursor(DictCursor)

    def __del__(self):
        if self.cursor:
            self.cursor.close()
            # print("关闭游标")
        if self.conn:
            self.conn.close()
            # print("关闭链接")

    # 执行增删改操作
    def execute(self, sql, data=None):
        result = self.cursor.execute(sql, data)
        self.conn.commit()
        return result

    # 执行查询操作
    def fetch(self, sql, data=None, limit='ALL'):
        self.cursor.execute(sql, data)
        if isinstance(limit, int):
            if limit == 1:
                return self.cursor.fetchone()
            else:
                return self.cursor.fetchmany(limit)
        else:
            return self.cursor.fetchall()


class EsOperation(object):
    def __init__(self, host, port=9200, user='', pwd=''):
        self.es = self.get_conn(host, port, user, pwd)

    def __del__(self):
        self.es.close()

    def __repr__(self):
        return '连接成功'

    def get_conn(self, host, port=9200, user='', pwd=''):
        es = Elasticsearch(hosts=host, port=port, sniff_on_start=True,
                           sniff_on_connection_fail=True,
                           sniff_timeout=60,
                           http_auth=(user, pwd),
                           timeout=120)
        return es

    def insert_one_data(self, index, body={}, id=get_current_time_str() + get_random_str()):
        return self.es.index(index=index, doc_type="_doc", id=id, body=body)

    def insert_many_data(self, index: str, data_list: list):

        def get_chunked_data(data, length):
            for i in range(0, len(data), length):
                yield data[i:i + length]

        for chunk_list in get_chunked_data(data_list, 1000):
            actions = [
                {"_index": index, "_id": get_current_time_str() + get_random_str(), "_source": data}
                for data in chunk_list]
            a = helpers.bulk(self.es, actions)
            print(a[1])
        return True

    def delete_data(self, index, query=None, id=None):
        if id:
            return self.es.delete(index, id)
        return self.es.delete_by_query(index, body=query)

    def update_data(self, index, id=None, body={}):
        if id:
            return self.es.update(index, id, body=body)
        return self.es.update_by_query(index, body=body)

    def get_count(self, index, query=None):
        """
        获取满足条件的数据总数
        :param index:索引
        :param query:查询条件
        :return:数据总数
        """
        return self.es.count(index=index, body=query).get('count')

    def query_all_data(self, index, query, scroll='5m', size=1000):
        """
        获取所有满足条件的数据
        :param index:索引
        :param query:查询条件
        :param scroll:设置游标查询窗口保持时间，默认5分钟
        :param size:单次查询数量，默认1000条
        :return:查询结果集列表
        """
        result = []
        search_result = self.es.search(index=index, body=query, scroll=scroll, size=size)
        result = search_result.get("hits").get("hits")
        scroll_id = search_result["_scroll_id"]
        total = search_result["hits"]["total"]["value"]
        for i in range(int(total / size)):
            res = self.es.scroll(scroll_id=scroll_id, scroll=scroll)  # scroll参数必须指定否则会报错
            result += res["hits"]["hits"]
        return result

    def query_data(self, index, query):
        result = self.es.search(index=index, body=query)
        return result


class MongoDB(object):
    def __init__(self, host, port=27017):
        self.client = pymongo.MongoClient(host=host, port=port)

    def db(self,db_name):
        return self.client.get_database(db_name).get_collection()

    def collection(self,col_name):
        pass



client = pymongo.MongoClient(host='192.168.0.178', port=27017)

dev = client.dev

for x in dev['demo'].find({}, {"alexa": 0}):
    print(x)

db = client.get_database('test')

users = db.get_collection('users.db')
person = {'name': 'zone', 'sex': 'boy'}
persons = [{'name': 'zone', 'sex': 'boy'}, {'name': 'zone', 'sex': 'boy1'}, {'name': 'qone', 'sex': 'girl'},
           {'name': 'qone1', 'sex': 'girl'}]

users.insert(person)
users.insert_many(persons)
# users.drop()
for x in users.find():
    print(x)

# pool = redis.ConnectionPool(host='192.168.0.178', port=16379, password='123456')
# red = redis.Redis(connection_pool=pool)
# key = 'str_value'
# red.set(key, string_value)
# print(red.get(key).decode())
#
# print(red.strlen(key))
#
# print(red.getrange(key, 0, 3))
#
# key = "list_value"
# # for x in init_list:
# #     red.lpush(key,x)
#
# # red.lpop(key)
# # red.rpop(key)
# # lambda x: red.lpush(key, x)(x for x in init_list)
#
# import json
#
# print(red.lrange(key, 0, -1))
#
# print(red.llen(key))
#
# key = 'set_value'
# red.sadd(key, 'set21', 123, 'fhisfdh')
# print(red.scard(key))
# red.sadd(key, 'fhsadjkg')
# print(red.srem(key, 123))
# print(red.smembers(key))
#
# key = 'zset_value'
# red.zadd(key, {"a1": 6, "a2": 2, "a3": 5})
# print(red.zcard(key))
# print(red.zrank(key, 'a1'))
# # red.zadd(key,init_dict)
# # print(red.zcard(key))
#
# key = 'hash_value'
#
# red.hset(key, 'init_dict', json.dumps(init_dict))
#
# a = json.loads(red.hget(key, 'init_dict'))
# print(a)
# print(type(a))
