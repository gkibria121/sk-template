from mongomock import MongoClient
import regex as re
import json
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


        documents = json.dumps(data, indent=4)

        if type(data) == dict:
            self.tables = self.tables +f'''
{table}.insert_one({documents})
'''
        if type(data) == list:
            self.tables = self.tables +f'''
{table}.insert_many({documents})
'''
    def set_primary_table(self,name):
        self.primary_table = name


    def select(self,project):


        if '$group' in self.group:
            self.select_with_group(project)
        else:
            self.project = {'$project' : project}
            self.pipeline.append(self.project)

    def where(self,match):


        self.match = {'$match': match}
        self.pipeline.append(self.match)

    def group(self, group):

        self.group = {'$group':  group }

    def sort(self, sort):

        self.sort = {'$sort': sort}
        self.pipeline.append(self.sort)

    def join(self,joints):
        for join in joints:
            from_table,right,local,foreign = join

            self.lookup ={
            '$lookup' : {
            'from' : from_table,
            'localField' : local,
            'foreignField' : foreign,
            'as' :  right
            }
            }
            self.pipeline.append(self.lookup)
            if not right.endswith('_'):
                self.pipeline.append({'$unwind' : f"${right}"})


    def select_with_group(self,project):
            # merge group with select
            temp_project ={}
            temp_project.update(project)
            temp_project['_id']  = self.group['$group']['_id']

            temp = {}
            uniqe_temp = {}

            for key,value in temp_project.items():
                if key!= '_id' and (type(value)==str or value==1) and value not in temp_project['_id'].values():
                    temp2 = value  if value != 1 else f"${key}"
                    temp[key] = {'$first' : temp2}
                elif key=='_id':
                    temp[key] = value
                elif value in temp_project['_id'].values():

                    uniqe_temp[key] = re.sub(r'(\$)\b','$_id.',value)

                else:
                    temp[key] = value

            self.group['$group'] = temp
            self.pipeline.append(self.group)




            ## select with uniqe ides
            temp  = {}
            for key,value in project.items():
                temp[key] = f'${key}'
            if '_id' not in temp:
                temp['_id'] = 0

            temp.update(uniqe_temp)

            self.project = {'$project' : temp}
            self.pipeline.append(self.project)


    def run(self):

        if '$project' not in self.project:
            self.pipeline.append({'$project' : {'_id' : 0}})

        self.pipeline = json.dumps( self.pipeline, indent=4)

        script =  f'''
from mongomock import MongoClient as MockMongoClient


client = MockMongoClient()
db = client['test_database']
{self.tables}
result = []
pipeline = {self.pipeline}
for item in {self.primary_table}.aggregate(pipeline):
    result.append(item)
print(result)

'''
        print(script)
        return script

    def clear(self):
        self.project = {}
        self.match = {}
        self.pipeline = []
        self.primary_table = ''
        self.tables =''''''
        self.lookup = {}

##sk_mongo = MongoController()

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
##sk_mongo.join([('comment' , 'id' , 'postId'),('post' , 'id' , 'CommentId')])
##
##result = sk_mongo.run()
##
##print(result)




