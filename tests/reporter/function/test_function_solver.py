import unittest

from sk_report_generator.reporter.function_solver.function_solver import FunctionSolver
from sk_report_generator.reporter.function_solver.single_function_solver import SingleFunctionSOlver
from sk_report_generator.reporter.function_solver.process_function_calling import ProcessFunctionCalling


class TestFunctionSolver(unittest.TestCase):
    def setUp(self):
        self.function_solver = FunctionSolver()
        self.single_function_solver = SingleFunctionSOlver()
        self.process_function_calling = ProcessFunctionCalling()
        self.function_solver.set_single_obj_solver( self.single_function_solver )
        self.function_solver.set_process_function_calling(self.process_function_calling)


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

if __name__=='__main__':
    unittest.main()