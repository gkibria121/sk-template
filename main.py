from calculator.sk_calculator import Calculator
from data.sk_data.data import DataStructure
from reporter.sk_report_generator import ReportGenerator
import json

class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.reporter = ReportGenerator()
        self.data_structure = DataStructure()
        self.data_structure.set_calculator(self.calculator)

        self.reporter.set_reporter(self.reporter)

    def get_data(self, declaration_string):
        data_structure = self.data_structure.run(declaration_string)
        return data_structure

    def get_report(self, template, data):
        self.reporter.set_reporter(self.reporter)
        return self.reporter.generate_report(template, data)

    def get_declarations(self, text):
        declarations = self.declaration_process.process(text)
        return declarations


Controller = Controller()

data = Controller.get_data('''
$x = 5;$y = $x+3;$z = $y*2;
''')
print(data)

template = '''
{{$z:b}}
'''
declaration = Controller.get_report(template, data)
print(declaration)
