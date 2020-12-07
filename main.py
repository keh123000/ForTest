import pymongo

client = pymongo.MongoClient(host='192.168.0.178', port=27017)

dev = client.dev
#
# for x in dev['demo'].find():
#     print(x)

col = dev.get_collection('demo')
data = {
    'adc': {"name": "zhangsan", "age": 18},
    'ap': {"name": "lisi", "age": 20},
    'hh': {
        'adc': {"name": "zhangsan", "age": 18},
        'ap': {"name": "lisi", "age": 20},

        'jbk': {
            'adc': {"name": "zhangsan", "age": 18},
            'ap': {"name": "lisi", "age": [23, 24]}
        }
    }
}
# col.insert(data)
for x in dev['demo'].find():
    print(x)

db = client.get_database('test')

users = db.get_collection('users.db')
