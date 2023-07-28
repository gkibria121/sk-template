from calculator.sk_calculator import Calculator
from variable.sk_variable_handler.variable_handler import VariableHandler
from reporter.sk_report_generator import ReportGenerator
from random_variable.sk_random_variable import RandomVariableGenerator
from table.sk_table_hanlder import TableHandler

import json
class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.variable = VariableHandler()
        self.variable.set_calculator(self.calculator)
        self.reporter = ReportGenerator()
        self.random_variable_generator = RandomVariableGenerator()

        self.table_hanlder = TableHandler()

        self.reporter.set_reporter(self.reporter)

    def get_data(self, declaration_string):
        random_variable = self.random_variable_generator.process(declaration_string)
        solved_table = self.table_hanlder.run(random_variable)
        return self.variable.get_result(solved_table)

    def get_report(self, template, data):
        self.reporter.set_reporter(self.reporter)
        return self.reporter.generate_report(template, data)

    def get_declarations(self, text):
        declarations = self.declaration_process.process(text)
        return declarations


Controller = Controller()

##print(Controller.get_data('''
##$x= random_json();
##$table= [{'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}];
##$table2 = $table(x)=>{ {'number' : $table<[$parent_index-1].number|1>+$table<[$parent_index+1].number|1> } };
##'''))

data = {'$x' : 1}

template = '''
{{$x:((x)=>x==1),c1,c4}}
{{$x:((x)=>x==1),c2,c4|c3,c4}}
{{$x:((x)=>x!=1),c2,c4|c3,c4}}
<format>
c1= {'align' : 'center' }
c2 = {'align' : 'left'}
c3 = {'align' : 'right'}
c4 = {'width' : 30, 'fill' : '0'}
</format>
'''
declaration = Controller.get_report(template, data)
print(declaration)
