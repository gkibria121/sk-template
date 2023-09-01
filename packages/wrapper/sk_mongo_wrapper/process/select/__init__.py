import regex as re
from .operators import  OperatorsProcess
class SelectProcess:
    def __init__(self):
        self.go_next = None
        self.operators_process = OperatorsProcess()

    def process(self,name,argument):

        if name =='select':

            pattern =r'\:\s*(?![\"\'])((\d+(\.\d+))|([\w\.\s\+\-\/\*\^\%\(\)]+))(?![\"\'])'


            argument = re.sub(pattern , lambda match : f": {self.operators_process.run(match[4])}" if match[3] == None else  f": {match[2]}",argument)

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table
    def set_argument_process(self,argument_processor):
        self.argument_processor = argument_processor
        self.operators_process.set_argument_process(self.argument_processor)
