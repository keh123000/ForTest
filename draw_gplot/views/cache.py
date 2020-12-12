from common.redis_db import redis
import json


class NodesCache(object):
    pass

def cache_add_graph_data(types='nodes', data=None, user_id=None):
    """
    添加节点或连线信息至
    :param types: 插入的信息类型 nodes 表示节点，links 表示链接关系
    :param data: 要插入缓存的数据内容
    :param user_id: 信息所属用户ID
    :return:
    """
    red_key = 'graph_%s_%s' % (types, user_id)

    if isinstance(data, dict):
        # 如果是单个字典对象
        redis.hset(types, data.get('_id'), json.dumps(data))
        redis.rpush(red_key, data.get('_id'))
    elif isinstance(data, list):
        add_ids = []
        for sub in data:
            redis.hset(types, sub.get('_id'), json.dumps(sub))
            add_ids.append(sub.get('_id'))
        if not redis.exists(red_key):
            for id in add_ids:
                redis.rpush(red_key, id)
    return 1

# def cache_add_nodes(node):
