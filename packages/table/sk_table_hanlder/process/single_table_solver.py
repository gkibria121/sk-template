import regex as re

class SingleTableSolver:
    def __init__(self):
        self.wrapper = None
        self.mongo_controller = None

    def run(self,data,variable):
        variable_name = variable[0]
        table_expression = variable[1]
        pattern = r'\$<((\w+(\:\w+))(,(\w+(\:\w+)))*)>((\w+(\((([^()]|(?9)))*\)))(->(\w+(\((([^()]|(?9)))*\))))*)'
        match = re.search(pattern , table_expression)
        if match:
            table_names = [item for index,item in enumerate(match[1].split(',')) if item !='']
            self.wrapper.set_table_data(data,table_names)
            table_queries = self.get_query_list(match[7])

            queries = self.wrapper.process_queries(table_queries)

            script = self.wrapper.query(queries)

            result = self.wrapper.evaluate(script)

            return result

        return -1

    def get_query_list(self,queries):

        queries = [item for index,item in enumerate( re.split(r'->',queries)) if item!='']

        return queries

    def set_wrapper(self,wrapper):
        self.wrapper = wrapper

    def set_mongo_controller(self,controller):
        self.mongo_controller = controller
        self.wrapper.set_mongo_controller(self.mongo_controller)


