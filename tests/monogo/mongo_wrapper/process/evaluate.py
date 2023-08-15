import unittest
from sk_mongo_wrapper.process.evaluate import EvaluateScript

class TestEvaluate(unittest.TestCase):

    def setUp(self):
        self.evaluate_script = EvaluateScript()


    def test_evaluate(self):
        script = 'print("hello, world")'
        result = self.evaluate_script.run(script)
        self.assertEqual(result,'hello, world')

        script = '''
from mongomock import MongoClient as MockMongoClient
client = MockMongoClient()
db = client['test_database']
x = db['x']
x.insert_many([{'name': 'kibria', 'age': 23, 'y': {'id': 1}}, {'name': 'sumu', 'age': 23, 'y': {'id': 1}}, {'name': 'mehedi', 'age': 21, 'y': {'id': 2}}, {'name': 'sithi', 'age': 21, 'y': {'id': 2}}])
result = []
for item in x.aggregate([{'$sort': {'y.id': -1, 'name': -1}}, {'$project': {'_id': 0}}]):
    result.append(item)
print(result)
'''
        result = self.evaluate_script.run(script)
        self.maxDiff = None
        self.assertEqual(result,"[{'name': 'sithi', 'age': 21, 'y': {'id': 2}}, {'name': 'mehedi', 'age': 21, 'y': {'id': 2}}, {'name': 'sumu', 'age': 23, 'y': {'id': 1}}, {'name': 'kibria', 'age': 23, 'y': {'id': 1}}]")


    def test_mongo_script(self):

        script = '''
from mongomock import MongoClient as MockMongoClient


client = MockMongoClient()

db = client['test_database']


x = db['x']
x.insert_many([{'name': 'kibria', 'age': 23, 'y': {'id': 1}}, {'name': 'sumu', 'age': 23, 'y': {'id': 1}}, {'name': 'mehedi', 'age': 21, 'y': {'id': 2}}, {'name': 'sithi', 'age': 21, 'y': {'id': 2}}])



result = []

for item in x.aggregate([{'$group': {'totalId': {'$sum': '$y.id'}, '_id': {'age': '$age', 'name': '$name'}}}, {'$project': {'totalId': '$totalId', 'name': '$_id.name', 'age': '$_id.age', '_id': 0}}, {'$project': {'_id': 0}}]):
    result.append(item)


print(result)
'''
        result = self.evaluate_script.run(script)
        self.maxDiff = None
        self.assertEqual(result,"[{'totalId': 2, 'name': 'mehedi', 'age': 21}, {'totalId': 2, 'name': 'sithi', 'age': 21}, {'totalId': 1, 'name': 'kibria', 'age': 23}, {'totalId': 1, 'name': 'sumu', 'age': 23}]")
        script = '''
from mongomock import MongoClient as MockMongoClient


client = MockMongoClient()

db = client['test_database']


x = db['x']
x.insert_many([{'name': 'kibria', 'age': 23, 'y': {'id': 1}}, {'name': 'sumu', 'age': 23, 'y': {'id': 1}}, {'name': 'mehedi', 'age': 21, 'y': {'id': 2}}, {'name': 'sithi', 'age': 21, 'y': {'id': 2}}])



result = []

for item in x.aggregate([
    {
        "$group": {
            "totalId": {
                "$sum": "$y.id"
            },
            "_id": {
                "age": "$age",
                "name": "$name"
            }
        }
    },
    {
        "$project": {
            "totalId": "$totalId",
            "name": "$_id.name",
            "age": "$_id.age",
            "_id": 0
        }
    },
    {
        "$project": {
            "_id": 0
        }
    }
]):
    result.append(item)


print(result)
'''
        result = self.evaluate_script.run(script)
        self.maxDiff = None
        self.assertEqual(result,"[{'totalId': 2, 'name': 'mehedi', 'age': 21}, {'totalId': 2, 'name': 'sithi', 'age': 21}, {'totalId': 1, 'name': 'kibria', 'age': 23}, {'totalId': 1, 'name': 'sumu', 'age': 23}]")






if __name__=="__main__":
    unittest.main()

