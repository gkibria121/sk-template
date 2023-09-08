from packages.calculator.sk_calculator import Calculator
from packages.data.sk_data_handler.data import DataStructure
from packages.reporter.sk_report_generator import ReportGenerator
from packages.variable.sk_variable_handler.variable_handler import VariableHandler
from packages.random_variable.sk_random_variable import RandomVariableGenerator
from packages.table.sk_table_hanlder import TableHandler
from packages.controller.sk_mongo_controller.sk_mongo_controller import MongoController
from packages.wrapper.sk_mongo_wrapper.sk_mongo_wrapper import MongoWrapper
from packages.function.sk_function_solver.function_solver import FunctionSolver
from packages.function.sk_function_solver.process_function_calling import ProcessFunctionCalling
from packages.function.sk_function_solver.single_function_solver import SingleFunctionSOlver
from packages.function.sk_function_solver.get_index_value import GetIndexValue
from packages.function.sk_function_solver.process_condition import ProcessCondition
import json
class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.data_structure = DataStructure()
        self.variable = VariableHandler()
        self.variable.set_function_solver(FunctionSolver())
        self.variable.set_get_index(GetIndexValue())
        self.variable.set_process_condition(ProcessCondition())
        self.variable.set_process_function_calling(ProcessFunctionCalling())
        self.variable.set_single_function_solver(SingleFunctionSOlver())


        self.random = RandomVariableGenerator()
        self.mongo_controller = MongoController()
        self.mongo_wrapper = MongoWrapper()
        self.table_handler = TableHandler()
        self.table_handler.set_wrapper(self.mongo_wrapper)
        self.table_handler.set_mongo_controller(self.mongo_controller)

        self.reporter = ReportGenerator()
        self.reporter.set_reporter(self.reporter)


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
$x =[1,2,3,4,-2];
$y = $x.first_index_of(-2);
$a = $x.index_of(-2);
$z = $x.last_index_of(2);
$b = $x.find((x)=> x>1);
$c = $x.find_first((x)=> x>1);
$d = $x.find_last((x)=> x>1);
$f = $x.in(1);
$g = $x.in(5);
$temp = 1;
$gg = $x.in($temp);
$arr = [1,2,3,4,5,6];
$new_one = [{x : 1},{x : 2}];
$arr_test = $<new_one:x>select({x : x.x})->where(x.x>1);
$new = $<arr:x>select( {id:x ,val:x*2},x )->where(x.id>1);
'''
##data = {'$table': [{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'department': 'Sales', 'salary': 50000.0, 'hire_date': '2020-01-15'}, {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'age': 35, 'department': 'HR', 'salary': 60000.0, 'hire_date': '2019-05-20'}, {'id': 3, 'first_name': 'Michael', 'last_name': 'Johnson', 'age': 28, 'department': 'IT', 'salary': 55000.0, 'hire_date': '2021-03-10'}, {'id': 4, 'first_name': 'Sarah', 'last_name': 'Williams', 'age': 32, 'department': 'Marketing', 'salary': 58000.0, 'hire_date': '2018-09-01'}, {'id': 5, 'first_name': 'David', 'last_name': 'Brown', 'age': 29, 'department': 'Finance', 'salary': 52000.0, 'hire_date': '2022-02-28'}]}
##template = '''<><<{{$table[0].id}}>> </>'''
data = controller.get_data(data)
print(data)
##declaration = controller.get_report(template, data)
##print(declaration)
