import pymongo

client = pymongo.MongoClient(host='192.168.0.178',port=27017)

dev = client.dev

for x in dev['demo'].find({},{ "alexa": 0 }):
  print(x)


db = client.get_database('test')

users = db.get_collection('users.db')
person = {'name': 'zone', 'sex': 'boy'}
persons = [{'name': 'zone', 'sex': 'boy'}, {'name': 'zone', 'sex': 'boy1'}, {'name': 		 'qone', 'sex': 'girl'}, {'name': 'qone1', 'sex': 'girl'}]

users.insert(person)
users.insert_many(persons)
# users.drop()
for x in users.find():
    print(x)

