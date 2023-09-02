from packages.calculator.sk_calculator import Calculator
from packages.data.sk_data_handler.data import DataStructure
from packages.reporter.sk_report_generator import ReportGenerator
from packages.variable.sk_variable_handler.variable_handler import VariableHandler
from packages.random_variable.sk_random_variable import RandomVariableGenerator
from packages.table.sk_table_hanlder import TableHandler
from packages.controller.sk_mongo_controller.sk_mongo_controller import MongoController
from packages.wrapper.sk_mongo_wrapper.sk_mongo_wrapper import MongoWrapper

import json

class Controller:

    def __init__(self):
        self.calculator = Calculator()
        self.data_structure = DataStructure()
        self.variable = VariableHandler()
        self.random = RandomVariableGenerator()
        self.mongo_controller = MongoController()
        self.mongo_wrapper = MongoWrapper()
        self.table_handler = TableHandler()
        self.table_handler.set_wrapper(self.mongo_wrapper)
        self.table_handler.set_mongo_controller(self.mongo_controller)
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
$land_area=10.0*720;
$story=9;
$floor_area=$land_area*0.80;
$total_floor_area=$floor_area*$story;
$cost_per_sft=2200;
$build_cost_lac=$total_floor_area*$cost_per_sft/100000;
$sale_area=$total_floor_area*0.5;
$no_of_parking=20;
$signing_lac=80;
$total_cost=$build_cost_lac+$signing_lac;
$sale_rate=5500;
$apt_sale=$sale_rate*$sale_area/100000;
$parking_sale=$no_of_parking*5/2.0;
$total_sale=$apt_sale+$parking_sale;
$gross_profit=$total_sale-$total_cost;
$sale=1425.6;
$cost=1220.48;
$profit=$sale-$cost;
'''
##template = '''{{::template,{'$user' : '$person'}}}
##{{::sub/template2,{'$user' : '$person2'}}}
##{{::sub/sub2/template3,{'$user' : '$person3'}}}
## '''
data = controller.get_data(data)
print(data)
##declaration = controller.get_report(template, data)
##print(declaration)
