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
        self.function_solver =FunctionSolver()







        self.random = RandomVariableGenerator()
        self.mongo_controller = MongoController()
        self.mongo_wrapper = MongoWrapper()
        self.table_handler = TableHandler()

        self.table_handler.set_wrapper(self.mongo_wrapper)
        self.table_handler.set_mongo_controller(self.mongo_controller)

        self.reporter = ReportGenerator()
        self.reporter.set_function_solver(self.function_solver)
        self.reporter.set_reporter(self.reporter)


        self.variable.set_calculator(self.calculator)

        self.data_structure.set_variable(self.variable)
        self.data_structure.set_random(self.random)
        self.data_structure.set_table_handler(self.table_handler)
        self.data_structure.set_function_solver(self.function_solver)



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
$boxes=[
  {Id:1, X:10,Y:20,Z:7},
  {Id:2, X:12,Y:15,Z:8},
  {Id:3, X:11,Y:22,Z:9},
  {Id:4, X:18,Y:12,Z:6},
  {Id:5, X:12,Y:6,Z:9},
];

$voulume_of_box()=>X*Y*Z;
$Top_of_box()=>Y*Z;
$Side_area_of_box()=>(X*Z+Y*Z)*2;

###caling of function
$box_volumes=$<boxes:x>select(
{
    Id:x.Id,
    volume:$voulume_of_box(x),
    top_area:$Top_of_box(x),
    side_area:$Side_area_of_box(x)
});

$triangles=[
   {a:12,b:7.5,c:9.81},
   {a:5.5,b:9.81,c:7.2},
   {a:8.3,b:4.51,c:6.85},
   {a:15,b:10.8,c:9.81}
];

$area_of_triangle()=> {
    s=a+b+c;
    return sqrt(s*(s-a)*(s-b)*(s-c));
};
$triangle_areas=$<triangles:x>select({ area:$area_of_triangle(x)});
$test= $unittest.test(voulume_of_box,(),[{id:"case1", data:{X:10,Y:20,Z:7.00000000001 }, expected:1400},{id:"case2", data:{X:10,Y:15,Z:5}, expected:750}]);
$test2= $unittest.test(voulume_of_box,(),[{id:"case1", data:{X:10,Y:20,Z:7.00000000001 },delta : 3, expected:1400},{id:"case2", data:{X:10,Y:15,Z:5}, expected:750}]);
'''
##data = {'$table': [{'id': 1, 'first_name': 'John', 'last_name': 'Doe', 'age': 30, 'department': 'Sales', 'salary': 50000.0, 'hire_date': '2020-01-15'}, {'id': 2, 'first_name': 'Jane', 'last_name': 'Smith', 'age': 35, 'department': 'HR', 'salary': 60000.0, 'hire_date': '2019-05-20'}, {'id': 3, 'first_name': 'Michael', 'last_name': 'Johnson', 'age': 28, 'department': 'IT', 'salary': 55000.0, 'hire_date': '2021-03-10'}, {'id': 4, 'first_name': 'Sarah', 'last_name': 'Williams', 'age': 32, 'department': 'Marketing', 'salary': 58000.0, 'hire_date': '2018-09-01'}, {'id': 5, 'first_name': 'David', 'last_name': 'Brown', 'age': 29, 'department': 'Finance', 'salary': 52000.0, 'hire_date': '2022-02-28'}]}
##template = '''<><<{{$table[0].id}}>> </>'''
data = controller.get_data(data)
print(data)
##declaration = controller.get_report(template, data)
##print(declaration)
