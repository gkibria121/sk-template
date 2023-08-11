import regex as re
from .process.group_by import GroupByProcess
from .process.join import JoinProcess
from .process.order_by import OrderByProcess
from .process.select import SelectProcess
from .process.where import WhereProcess
from .process.default import DefaultProcess



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
