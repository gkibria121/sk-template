from sk_report_generator.reporter.function_solver.function.max import Max
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestMax(unittest.TestCase):

    def setUp(self):
        self.max = Max()
        self.max.set_next(MethodDefault())

    def test_max(self):
        value = [1,2,3,4]
        method = 'max'
        condition = ''
        result = self.max.run(value,method,condition)
        self.assertEqual(result,4)


    def test_max_with_condition(self):
        value = [1,2,3,4]
        method = 'max'
        condition = '(x)=>x<4'
        result = self.max.run(value,method,condition)
        self.assertEqual(result,3)

if __name__=="__main__":
    unittest.main()