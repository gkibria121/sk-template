import unittest
from sk_function_solver.single_function_solver import SingleFunctionSOlver
from sk_function_solver.get_index_value import GetIndexValue
from sk_function_solver.process_condition import ProcessCondition
from sk_function_solver.single_function_solver import CustomFunction
from sk_function_solver.single_function_solver import Unittest
from sk_function_solver.function_solver import FunctionSolver
from sk_data_handler.data import DataStructure
class TestSingleFunctionSolver(unittest.TestCase):

    def setUp(self):
        self.single_function_solver = SingleFunctionSOlver()
        self.single_function_solver.set_get_index_value(GetIndexValue())
        self.single_function_solver.set_process_condition(ProcessCondition())


    def test_single_function_solver(self):
        self.single_function_solver.set_data({'$x':[1,2,3,4]})
        result = self.single_function_solver.run( '$x', '.reverse().sum()')
        self.assertEqual(result,'10')

        result = self.single_function_solver.run('$x', '.sum((x)=>x>1)')
        self.assertEqual(result,'9')
        self.single_function_solver.set_data({'({"key" : "value"})':[1,2,3,4]})
        result = self.single_function_solver.run('({"key" : "value"})', '.sum((x)=>x>1)')
        self.assertEqual(result,'9')

        self.single_function_solver.set_data({'$x': {'key' :[1,2,3,4] }})
        result = self.single_function_solver.run( '$x', '["key"].reverse().sum()')
        self.assertEqual(result,'10')

        self.single_function_solver.set_data({'$x': [{'name': 'Alice', 'age': 28},{'name': 'Bob', 'age': 32},{'name': 'Eve', 'age': 29}]})
        result = self.single_function_solver.run( '$x', '["age"]')
        self.assertEqual(result,'[28, 32, 29]')

        self.single_function_solver.set_data({'$x':{ 'key':  [{'name': 'Alice', 'age': 28},{'name': 'Bob', 'age': 32},{'name': 'Eve', 'age': 29}]}})
        result = self.single_function_solver.run( '$x', '["key"]["age"]')
        self.assertEqual(result,'[28, 32, 29]')






from sk_calculator import Calculator
from sk_calculator import Calculator
from sk_data_handler.data import DataStructure
from sk_report_generator import ReportGenerator
from sk_variable_handler.variable_handler import VariableHandler
from sk_random_variable import RandomVariableGenerator
from sk_table_hanlder import TableHandler
from sk_mongo_controller.sk_mongo_controller import MongoController
from sk_mongo_wrapper.sk_mongo_wrapper import MongoWrapper
from sk_function_solver.function_solver import FunctionSolver
from sk_function_solver.process_function_calling import ProcessFunctionCalling
from sk_function_solver.single_function_solver import SingleFunctionSOlver
from sk_function_solver.get_index_value import GetIndexValue
from sk_function_solver.process_condition import ProcessCondition

class TestCustomFunctionSolver(unittest.TestCase):

    def setUp(self):
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
        self.function_solver.set_ds_solver_chain(self.data_structure.comment_remover)






    def test_custom_function_solver(self):
        data = '''
        $volume_of_box($x,$y)=>$x.X*$y.Y;
        $test= $unittest.test(volume_of_box,($x,$y),[{id:"case1", data:{ $x : {X:10,Y:20,Z:7},$y : {X:10,Y:20,Z:7} }, expected:1400},{id:"case2", data:{ $x : {X:10,Y:20,Z:7},$y : {X:10,Y:20,Z:7} }, expected:200}]);
        '''
        result = self.data_structure.run(data)
        self.assertEqual(result,{'$test': [{'id': 'case1', 'result': 'Faild', 'expected': 1400, 'actual': 200}, {'id': 'case2', 'result': 'Passed', 'expected': 200, 'actual': 200}]})



    def test_unittest(self):
        data = '''
        $function_one($x)=>$x.X;
        $test= $unittest.test(function_one,($x),[{id:"case1", data:{ $x : {X:10,Y:20,Z:7} }, expected:1400},{id:"case2", data:{ $x : {X:10,Y:20,Z:7},$y : {X:10,Y:20,Z:7} }, expected:200}]);'''
        result = self.data_structure.run(data)
        self.assertEqual(result,{'$test': [{'id': 'case1', 'result': 'Faild', 'expected': 1400, 'actual': 10}, {'id': 'case2', 'result': 'Faild', 'expected': 200, 'actual': 10}]})



        data = '''
        $function_one($x)=> $x.key/2.0001;;
        $test= $unittest.test(function_one,($x),[{id:"case1", data:{ $x :{'key' : 2 } }, expected:1400 ,delta : 3},{id:"case2", data:{ $x :{'key' : 2 } }, expected:200 , delta : 2}]);'''
        result = self.data_structure.run(data)
        self.assertEqual(result,{'$test': [{'id': 'case1', 'result': 'Faild', 'expected': 1400, 'actual': 1.0}, {'id': 'case2', 'result': 'Faild', 'expected': 200, 'actual': 1.0}]})


if __name__=='__main__':
    unittest.main()


