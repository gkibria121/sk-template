import unittest
from sk_function_solver.single_function_solver import SingleFunctionSOlver
from sk_function_solver.get_index_value import GetIndexValue
from sk_function_solver.process_condition import ProcessCondition

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

if __name__=='__main__':
    unittest.main()


