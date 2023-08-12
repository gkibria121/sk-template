import regex as re
from .comparison import ProcessOperators
from .logical import LogicalOperatorsProcess
class WhereProcess:
    def __init__(self):
        self.go_next = None
        self.process_operators = ProcessOperators()
        self.logic_process = LogicalOperatorsProcess()
        self.logic_process.set_process_operators(self.process_operators)



    def process(self,name,argument):
        if name == 'where':

            argument = self.logic_process.process(argument)

            argument = self.primary_table_process(argument)


        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table

    def primary_table_process(self,argument):

        pattern = r'(((?<![\.\$])(\b)('+re.escape(self.primary_table)+r')\.))'
        return re.sub(pattern,'', argument)


