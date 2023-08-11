from mongomock import MongoClient
import regex as re

class MongoController:

    def __init__(self):
        self.project = {}
        self.match = {}
        self.pipeline = []
        self.primary_table = ''
        self.tables =''''''
        self.lookup ={}

    def set_table_data(self,name,data):

        if not re.search(re.escape(f'{name} = db["{name}"]'),self.tables):
            self.tables = self.tables +f"\n{name} = db['{name}']"
            self.insert_data(name,data)

        else:
            self.insert_data(name,data)

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

    def join(self,joints):
        for join in joints:
            right,local,foreign = join

            self.lookup ={
            '$lookup' : {
            'from' : right,
            'localField' : local,
            'foreignField' : foreign,
            'as' :  right if right.endswith('s') else f"{right}s"
            }
            }
            self.pipeline.append(self.lookup)

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
##        exec(script)

        return script

    def clear(self):
        self.project = {}
        self.match = {}
        self.pipeline = []
        self.primary_table = ''
        self.tables =''''''
        self.lookup = {}

##sk_mongo = SkMongo()
##
##sk_mongo.set_primary_table('post')
##sk_mongo.set_table('comment')
##sk_mongo.set_table('post')
##comments = open('comments.txt','r').read()
##posts = open('posts.txt','r').read()
##sk_mongo.insert_data('comment',eval(comments))
##sk_mongo.insert_data('post',eval(posts))
##sk_mongo.where({"userId" : 1})
##sk_mongo.select({"id" : 1 , "userId" : "$userId" , '_id' : 0 , 'title' : '$title' })
##sk_mongo.sort({'id' : -1})
##sk_mongo.group({'_id' :{'userId' : '$userId'} , 'totalId' : {'$sum' : '$id'} })
##sk_mongo.join('comment' , 'id' , 'postId')
##
##result = sk_mongo.run()

##print(result)




