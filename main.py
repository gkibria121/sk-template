from packages.calculator.sk_calculator import Calculator
from packages.data.sk_data_handler.data import DataStructure
from packages.reporter.sk_report_generator import ReportGenerator
from packages.variable.sk_variable_handler.variable_handler import VariableHandler
from packages.random_variable.sk_random_variable import RandomVariableGenerator
from packages.table.sk_table_hanlder import TableHandler
import json

class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.data_structure = DataStructure()
        self.variable = VariableHandler()
        self.random = RandomVariableGenerator()
        self.table_handler = TableHandler()
        self.reporter = ReportGenerator()


        self.variable.set_calculator(self.calculator)

        self.data_structure.set_random(self.variable)
        self.data_structure.set_variable(self.random)
        self.data_structure.set_table_handler(self.table_handler)



    def get_data(self, declaration_string):
        data_structure = self.data_structure.run(declaration_string)
        return data_structure

    def get_report(self, template, data):
        self.reporter.set_reporter(self.reporter)
        return self.reporter.generate_report(template, data)

    def get_declarations(self, text):
        declarations = self.declaration_process.process(text)
        return declarations


controller = Controller()
data = '''
$students = [
    {
        "student_id": 1,
        "name": "John Smith",
        "age": 18,
        "grade": "A"
    },
    {
        "student_id": 2,
        "name": "Emily Johnson",
        "age": 17,
        "grade": "B"
    },
    {
        "student_id": 3,
        "name": "Michael Williams",
        "age": 18,
        "grade": "A"
    },
    {
        "student_id": 4,
        "name": "Sophia Brown",
        "age": 16,
        "grade": "C"
    },
    {
        "student_id": 5,
        "name": "William Davis",
        "age": 17,
        "grade": "B"
    }
];
$attendance = [
    {
        "student_id": 1,
        "attendance": 4
    },
    {
        "student_id": 2,
        "attendance": 3
    },
    {
        "student_id": 3,
        "attendance": 5
    },
    {
        "student_id": 4,
        "attendance": 3
    },
    {
        "student_id": 5,
        "attendance": 3
    }
];

$students_with_attendance = $<students:x,attendance:y>join(attendance:x.student_id=y.student_id);
'''
##template = '''{{$table4}}'''
data = controller.get_data(data)
print(data)
##declaration = controller.get_report(template, data)
##print(declaration)
