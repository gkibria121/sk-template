from sk_calculator import Calculator
from sk_variable_handler.variable_handler import VariableHandler
from reporter.sk_report_generator import ReportGenerator
from sk_declaration import DeclarationGenerator


class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.variable = VariableHandler()
        self.variable.set_calculator(self.calculator)
        self.reporter = ReportGenerator()
        self.declaration_process = DeclarationGenerator()

    def get_data(self, declaration_string):
        return self.variable.get_result(self.declaration_process.process(declaration_string))

    def get_report(self, template, data):
        return self.reporter.generate_report(template, data)

    def get_declarations(self, text):
        declarations = self.declaration_process.process(text)
        return declarations


Controller = Controller()

# data = Controller.get_data(text)
data = {'$x': 40.6}
template = '''{{$x::{'align': 'left','fill' : '#','width' : 10}}}
{{$x::{'align': 'right','fill' : '0','width' : 10,'floor-precision' : 2}}}
'''
declaration = Controller.get_report(template, data)
print(declaration)
