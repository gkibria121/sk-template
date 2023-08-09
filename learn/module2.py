from mongomock import MongoClient as MockMongoClient


client = MockMongoClient()

db = client['test_database']


x = db["x"]

y = db["y"]

x.insert_many([{'x': 1, 'cat': 1}, {'x': 2, 'cat': 1}])

y.insert_many([{'y': 1}, {'y': 2}])

y.insert_one({'y': 3})



ans = []
result = x.aggregate([{'$group': {'_id': {'index':  '$cat'}, 'x': '$x'}}])
for item in  result:
    ans.append(item)


print(ans)