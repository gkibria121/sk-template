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
data = {'$x': 'gkibria is my name'}
template = '''{{$x.upper()}}'''
declaration = Controller.get_report(template, data)
print(declaration)
