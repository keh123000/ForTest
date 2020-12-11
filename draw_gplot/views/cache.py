from common.redis_db import redis
import json


def cache_add_graph_data(type='nodes', user_id=None, data=None):
    # def data_add(data):
    #     if isinstance(data, dict):
    #         redis.hset(type,data.get('id'),json.dumps(data))
    #     elif isinstance(data, list):
    #         for sub in data:
    #             print(sub)
    #             redis.hset(type, sub.get('id'), json.dumps(sub))
    # data_add(data)
    redis.hset(type, user_id, json.dumps(data))
