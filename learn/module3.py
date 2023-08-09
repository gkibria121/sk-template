from mongomock import MongoClient


class SkMongo:

    def __init__(self):
        self.project = {}
        self.match = {}
        self.pipeline = []
        self.primary_table = ''
        self.tables =''''''

    def set_table(self,name):
        self.tables = self.tables +f'''
{name} = db["{name}"]
'''

    def insert_data(self,table,data):
        if type(data) == dict:
            self.tables = self.tables +f'''
{table}.insert_one({data})
'''
        if type(data) == list:
            self.tables = self.tables +f'''
{table}.insert_many({data})
'''
    def set_primary_table(self,name):
        self.primary_table = name


    def select(self,project):


        self.project = {'$project' : project}
        self.pipeline.append(self.project)

    def where(self,match):


        self.match = {'$match': match}
        self.pipeline.append(self.match)

    def group(self, group):

        self.group = {'$group':  group }
        self.pipeline.append(self.group)

    def sort(self, sort):

        self.sort = {'$sort': sort}
        self.pipeline.append(self.sort)


    def run(self):

        script =  f'''
from mongomock import MongoClient as MockMongoClient


client = MockMongoClient()

db = client['test_database']

{self.tables}


result = []

for item in {self.primary_table}.aggregate({self.pipeline}):
    result.append(item)


print(result)

'''
        exec(script)

        return script





sk_mongo = SkMongo()
sk_mongo.set_primary_table('x')
sk_mongo.set_table('x')
sk_mongo.set_table('y')
sk_mongo.insert_data('x',[{'x' :1 ,'cat' : 1 },{'x' : 2,'cat' : 1 }])
sk_mongo.insert_data('y',[{'y' :1 },{'y' : 2}])
sk_mongo.insert_data('y',{'y' :3 })



sk_mongo.where({"x" : 2})
sk_mongo.select({"x" : "$x" , '_id' : 0 })
##sk_mongo.sort({'name' : 1})
##sk_mongo.group({'_id' :'$cat' , 'x' : '$x'})

result = sk_mongo.run()

##print(result)




