import unittest

from sk_function_solver.function_solver import FunctionSolver
from sk_function_solver.single_function_solver import SingleFunctionSOlver
from sk_function_solver.process_function_calling import ProcessFunctionCalling
from sk_function_solver.process_condition import ProcessCondition
from sk_function_solver.get_index_value import GetIndexValue


class TestFunctionSolver(unittest.TestCase):
    def setUp(self):
        self.function_solver = FunctionSolver()



    def test_function_solver(self):

        self.function_solver.set_data({'$x': [1,2,3,4]})
        result = self.function_solver.solve('$x.sum()')
        self.assertEqual(result,'10')

        self.function_solver.set_data({'$x': [1,2,3,4]})
        result = self.function_solver.solve('$x.avg()')
        self.assertEqual(result,'2.5')

        self.function_solver.set_data({'$x': [1,2,3,4]})
        result = self.function_solver.solve('$x.max()')
        self.assertEqual(result,'4')

        self.function_solver.set_data({'$x': [
    {

    'expenses':
          [
            { 'amount':100, 'sl_no':'01'},
        { 'amount':430, 'sl_no':'02'},
      ]
    },
    {

    'expenses':
          [
             { 'amount':700, 'sl_no':'03'},
         { 'amount':360, 'sl_no':'04'},
      ]
    }
]})
        result = self.function_solver.solve('$x.expenses.amount')
        self.assertEqual(result,'[100, 430, 700, 360]')

        result = self.function_solver.solve('$x.expenses.amount.sum()')
        self.assertEqual(result,'1590')
if __name__=='__main__':
    unittest.main()