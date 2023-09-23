import unittest
from sk_function_solver.single_function_solver import SingleFunctionSOlver
from sk_function_solver.get_index_value import GetIndexValue
from sk_function_solver.process_condition import ProcessCondition
from sk_function_solver.single_function_solver import CustomFunction
from sk_function_solver.single_function_solver import Unittest
from sk_function_solver.function_solver import FunctionSolver
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








class TestCustomFunctionSolver(unittest.TestCase):

    def setUp(self):

        self.custom_function = CustomFunction()
        self.custom_function.set_next(type('Default', (),{'run' : lambda value,method,conditon: value}))



    def test_custom_function_solver(self):
        name  = 'function_one'
        argument = ''
        code = 'return 1;'
        self.custom_function.create(name,argument,code)
        result = self.custom_function.run({'key' : 'value1'},name,argument)
        self.assertEqual(result,'1')



        code = 's = 1+2;y = s+1;return y;'
        self.custom_function.create(name,argument,code)
        result = self.custom_function.run({'key' : 'value1'},name,argument)
        self.assertEqual(result,'4')




class TestUnittest(unittest.TestCase):


    def setUp(self):

        self.function_solver =FunctionSolver()


    def no_test_unittest(self):
        name  = 'function_one'
        argument = ''
        code = 'return 1;'
        self.function_solver.create(name,argument,code)
        result = self.function_solver.unittest('.function_one()','',"[{'id' : 'case1', 'data' : {'key' : 2 }, 'expected' : 1 }]")
        self.assertEqual(result,[{'id': 'case1', 'result': 'Passed', 'expected': 1, 'actual': 1}])



        name  = 'function_one'
        argument = ''
        code = 'return key/2.0001;'
        self.function_solver.create(name,argument,code)
        result = self.function_solver.unittest('.function_one()','',"[{'id' : 'case1', 'data' : {'key' : 2 }, 'expected' : 1 }]")
        self.assertEqual(result,[{'id': 'case1', 'result': 'Faild', 'expected': 1, 'actual': 0.9999500024998749}])

        code = 'return key/2.0001;'
        self.function_solver.create(name,argument,code)
        result = self.function_solver.unittest('.function_one()','',"[{'id' : 'case1', 'data' : {'key' : 2 }, 'expected' : 1 ,'delta' : 3}]")
        self.assertEqual(result,[{'id': 'case1', 'result': 'Passed', 'expected': 1, 'actual': 1.0}])



        code = 'return 1 if x==1 else 2;'
        self.function_solver.create(name,argument,code)
        result = self.function_solver.unittest('.function_one()','',"[{'id' : 'case1', 'data' : {'x' : 1 }, 'expected' : 1 ,'delta' : 3}]")
        self.assertEqual(result,[{'id': 'case1', 'result': 'Passed', 'expected': 1, 'actual': 1}])

        code = 'return 1 if x==1 else 2;'
        self.function_solver.create(name,argument,code)
        result = self.function_solver.unittest('.function_one()','',"[{'id' : 'case1', 'data' : {'x' : 2 }, 'expected' : 2 ,'delta' : 3}]")
        self.assertEqual(result,[{'id': 'case1', 'result': 'Passed', 'expected': 2, 'actual': 2}])



if __name__=='__main__':
    unittest.main()


