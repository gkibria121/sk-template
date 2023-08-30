import unittest

from sk_report_generator.reporter.template.template_module import Moduler
from sk_report_generator.reporter.template.template_module import ReplaceFileReference
from sk_report_generator.reporter.template.template_module import GetFilesFromFolder
from sk_report_generator.reporter.template.template_module import ReplacePlaceHolderVariable




class TestFunctionSolver(unittest.TestCase):
    def setUp(self):
        self.function_solver = FunctionSolver()
        self.single_object_solver=SingleFunctionSOlver()
        self.single_object_solver.set_process_condition(ProcessCondition())
        self.single_object_solver.set_get_index_value(GetIndexValue())
        self.function_solver.set_single_obj_solver(self.single_object_solver)
        self.function_solver.set_process_function_calling(ProcessFunctionCalling())


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