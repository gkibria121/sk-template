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

            pattern = r'(\(([^()]+)\))'

            while True:
                if re.search(pattern,argument):
                    argument = re.sub(pattern,lambda match: self.logic_process.process(match[2]),argument)
                else:
                    argument = self.logic_process.process(argument)
                    break


            argument = self.argument_processor.process(argument)

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table

    def set_argument_process(self,argument_processor):
        self.argument_processor = argument_processor