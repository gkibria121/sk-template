from sk_report_generator.reporter.function_solver.function.min import Min
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestMin(unittest.TestCase):

    def setUp(self):
        self.min = Min()
        self.min.set_next(MethodDefault())

    def test_max(self):
        value = [1,2,3,4]
        method = 'min'
        condition = ''
        result = self.min.run(value,method,condition)
        self.assertEqual(result,1)


    def test_max_with_condition(self):
        value = [1,2,3,4]
        method = 'min'
        condition = '(x)=>x!=1'
        result = self.min.run(value,method,condition)
        self.assertEqual(result,2)

if __name__=="__main__":
    unittest.main()