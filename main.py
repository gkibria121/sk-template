from calculator.sk_calculator import Calculator
from variable.sk_variable_handler.variable_handler import VariableHandler
from reporter.sk_report_generator import ReportGenerator
from random_variable.sk_random_variable import RandomVariableGenerator
from table.sk_table_hanlder

import json
class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.variable = VariableHandler()
        self.variable.set_calculator(self.calculator)
        self.reporter = ReportGenerator()
        self.random_variable_generator = RandomVariableGenerator()

        self.reporter.set_reporter(self.reporter)

    def get_data(self, declaration_string):
        random_variable = self.random_variable_generator.process(declaration_string)
        return self.variable.get_result(random_variable)

    def get_report(self, template, data):
        self.reporter.set_reporter(self.reporter)
        return self.reporter.generate_report(template, data)

    def get_declarations(self, text):
        declarations = self.declaration_process.process(text)
        return declarations


Controller = Controller()

print(Controller.get_data('$x= random_json();'))

##data = {'$x' : [{"name": "John Doe","age": 30,"occupation": "Engineer"},{"name": "Jane Smith","age": 25,"occupation": "Teacher"},{"name": "Michael Johnson","age": 40, "occupation": "Doctor"},{"name": "Emily Williams","age": 22,"occupation": "Student"}]}
##template = '''
##{{$x.foreach(($y)=>{
##{{$y.name}}
##})}}
##'''
##declaration = Controller.get_report(template, data)
##print(declaration)
