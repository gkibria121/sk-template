import regex as re
class MongoWrapper:
    def __init__(self):
        self.mongo_controller = None
        self.primary_table = None
        self.query_process = QueryProcess()


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


class QueryProcess:

    def __init__(self):
        self.join_process = JoinProcess()
        self.select_process = SelectProcess()
        self.where_process = WhereProcess()
        self.group_process = GroupByProcess()
        self.order_process = OrderByProcess()
        self.default = DefaultProcess()


        self.join_process.set_next(self.select_process)
        self.select_process.set_next(self.where_process)
        self.where_process.set_next(self.group_process)
        self.group_process.set_next(self.order_process)
        self.order_process.set_next(self.default)

    def run(self,queries):
        temp = []
        for query in queries:
            pattern = r'([a-zA-Z_]+\w*)(\((([^()]|(?2))*)\))'
            match = re.search(pattern,query)
            if match:
                query_name = match[1]
                query_argument = match[3]

                name,argument = self.join_process.process(query_name,query_argument)

                temp.append(f"{name}({argument})")
        return temp

    def set_primary_table(self,table):
        self.join_process.set_primary_table(table)
        self.select_process.set_primary_table(table)
        self.where_process.set_primary_table(table)
        self.group_process.set_primary_table(table)
        self.order_process.set_primary_table(table)




class DefaultProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):

        return (name,argument)

    def set_next(self,go_next):

        self.go_next = go_next

    def set_primary_table(self,table):
        self.primary_table = table


class JoinProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):
        if name == 'join':
            temp = []
            join_list = [item for index,item in enumerate(argument.split(',')) if item != '']
            for join in join_list:
                pattern = r'(((?=\b)'+re.escape(self.primary_table)+r'\.([\w\.]+))|((?=\b)(\w+)\.([\w\.]+)))'
                result =  re.findall(pattern,join)
                right_table = result[0][4]
                local_id = result[1][2]
                foreign_id = result[0][5]
                temp.append((right_table,local_id,foreign_id))
            argument = temp

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table


class WhereProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):
        if name == 'where':
            pass

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table

class GroupByProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next

    def set_primary_table(self,table):
        self.primary_table = table

class OrderByProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next

    def set_primary_table(self,table):
        self.primary_table = table

class SelectProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table



