from calculator.sk_calculator import Calculator
from variable.sk_variable_handler.variable_handler import VariableHandler
from reporter.sk_report_generator import ReportGenerator
from declaration.sk_declaration import DeclarationGenerator


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
        self.reporter.set_reporter(self.reporter)
        return self.reporter.generate_report(template, data)

    def get_declarations(self, text):
        declarations = self.declaration_process.process(text)
        return declarations


Controller = Controller()

##print(Controller.get_data('x= c1(1+2)'))

data = {'$x':
    {
        "name": "Sophia Brown",
        "age": 20,
        "gender": "Female",
        "major": "Psychology",
        "gpa": 3.9
    }
}
template =  '''
{{$x.foreach(($key)=>{
    ------------------------------
    |{{$key::{'align' : 'center','width' : 30}}}|
     ------------------------------
})}}
'''
declaration = Controller.get_report(template, data)
print(declaration)
