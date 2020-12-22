import redis
from common.test_data import *
from common.utils import *

pool = redis.ConnectionPool(host='192.168.0.178', port=16379, password='123456')
red = redis.Redis(connection_pool=pool)
key = 'str_value'
red.set(key, string_value)
print(red.get(key).decode())

print(red.strlen(key))

print(red.getrange(key, 0, 3))

key = "list_value"
# for x in init_list:
#     red.lpush(key,x)

# red.lpop(key)
# red.rpop(key)
# lambda x: red.lpush(key, x)(x for x in init_list)

import json

print(red.lrange(key, 0, -1))

print(red.llen(key))


key = 'set_value'
red.sadd(key,'set21',123,'fhisfdh')
print(red.scard(key))
red.sadd(key,'fhsadjkg')
print(red.srem(key,123))
print(red.smembers(key))


key= 'zset_value'
red.zadd(key,{"a1":6, "a2":2,"a3":5})
print(red.zcard(key))
print(red.zrank(key,'a1'))
# red.zadd(key,init_dict)
# print(red.zcard(key))

key = 'hash_value'

red.hset(key,'init_dict',json.dumps(init_dict))

a = json.loads(red.hget(key,'init_dict'))
print(a)
print(type(a))

