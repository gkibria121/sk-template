import regex as re
from .query_process import QueryProcess
from .process.evaluate import EvaluateScript
class MongoWrapper:
    def __init__(self):
        self.mongo_controller = None
        self.primary_table = None
        self.query_process = QueryProcess()
        self.evaluate_script = EvaluateScript()
        self.data = None



    def set_mongo_controller(self,controller):
        self.mongo_controller = controller

    def set_table_data(self,data, tables):
        self.mongo_controller.set_primary_table(self.get_table_placeholder(tables[0]))
        self.primary_table = self.get_table_placeholder(tables[0])
        for table in tables:
            table_name = self.get_table_name(table)
            table_placeholder = self.get_table_placeholder(table)
            self.mongo_controller.set_table_data(table_placeholder,data[table_name])

    def get_table_placeholder(self,table):

        if ':' not in table:
            return table.replace('$','')

        table_names = table.split(':')
        return table_names[1]

    def get_table_name(self,table):
        table = table if table.startswith('$') else f"${table}"

        if ':' not in table:
            return table
        tables = table.split(':')
        return tables[0]


    def query(self,queries):
        for query in queries:
            match = re.search(r'([a-zA-Z_]+)\w*(\((([^()]|(?2))*)\))',query)
            if match:
                query_name = match[1]
                query_argument = match[3]
                query_function = getattr(self.mongo_controller,query_name)
                query_function(eval(query_argument))


        result = self.mongo_controller.run()
        return result



    def process_queries(self,queries):
        self.query_process.set_primary_table(self.primary_table)

        return self.query_process.run(queries)


    def evaluate(self,query):

        return self.evaluate_script.run(query)



