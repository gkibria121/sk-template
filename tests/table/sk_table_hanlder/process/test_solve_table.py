from sk_function_solver.function_solver import FunctionSolver
from sk_table_hanlder.process.single_table_solver import SingleTableSolver
from sk_mongo_controller.sk_mongo_controller import MongoController
from sk_mongo_wrapper.sk_mongo_wrapper import MongoWrapper
import unittest

class TestSingleTableSolver(unittest.TestCase):


    def setUp(self):
        self.single_table_solver = SingleTableSolver()
        self.single_table_solver.set_function_solver(FunctionSolver())
        self.single_table_solver.set_wrapper(MongoWrapper())
        self.single_table_solver.set_mongo_controller(MongoController())


    def test_single_solver(self):
        result = self.single_table_solver.run({'$array' : [1,2,3,4]},('$array','$<array:z>select({"x" : z})'))
        self.assertEqual(result,"[{'x': 1, }, {'x': 2, }, {'x': 3, }, {'x': 4, }]")

        result = self.single_table_solver.run({'$array' : [1,2,3,4]},('$array','$<array:z>select({"x" : ([1,2,3,4,5]).max()})'))
        self.assertEqual(result,"[{'x': 5, }, {'x': 5, }, {'x': 5, }, {'x': 5, }]")
        result = self.single_table_solver.run({'$array' : [{'x': 5, }, {'x': 5, }, {'x': 5, }, {'x': 5, }]},('$array','$<array:z>select({"x" :x})'))
        self.assertEqual(result,"[{'x': 5}, {'x': 5}, {'x': 5}, {'x': 5}]")

if __name__=='__main__':
    unittest.main()