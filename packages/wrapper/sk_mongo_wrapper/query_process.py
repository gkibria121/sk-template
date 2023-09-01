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

        self.argument_process = ArgumentProcess()
        self.set_argument_process(self.argument_process)

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
        self.argument_process.set_primary_table(table)
        self.join_process.set_primary_table(table)



    def set_argument_process(self,argument_processor):
        self.join_process.set_argument_process(argument_processor)
        self.select_process.set_argument_process(argument_processor)
        self.where_process.set_argument_process(argument_processor)
        self.group_process.set_argument_process(argument_processor)
        self.order_process.set_argument_process(argument_processor)


class ArgumentProcess:

    def __init__(self):

        self.key_process = KeyProcess()
        self.primary_table_process = PrimaryTableProcess()

        self.key_process.set_next (self.primary_table_process)

        self.primary_table_process.set_next(type('Defualt' , (),{'process' : lambda argument : argument}))

    def process(self,argument):
        result = self.key_process.process(argument)
        try:

            return eval(result)
        except NameError:
            return result
        except SyntaxError:
            return result
    def set_primary_table(self,table):
        self.primary_table = table
        self.key_process.set_primary_table(self.primary_table)
        self.primary_table_process.set_primary_table(self.primary_table)

class KeyProcess:

    def process(self,argument):

        pattern = r'(((?<![\.\$])(\b)('+re.escape(self.primary_table)+r')\.))'
        result =re.sub(pattern,'', argument)
        return self.go_next.process(result)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_primary_table(self,table):
        self.primary_table = table


class PrimaryTableProcess:

    def process(self,argument):

        pattern =r'\:\s*((?![\'\"])\b((\d+(?:\.\d+)?)|([\$\w\.]+))\b(?![\'\"]))'

        argument = re.sub(pattern , lambda match : f": \"${match[4]}\"" if match[3] == None else  f": {match[3]}",argument)

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table


