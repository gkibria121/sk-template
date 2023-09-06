from sk_function_solver.function.avg import Avg
from sk_function_solver.function.default import MethodDefault
import unittest

class TestAvg(unittest.TestCase):

    def setUp(self):
        self.avg = Avg()
        self.avg.set_next(MethodDefault())

    def test_avg(self):
        value = [1,2,3,4]
        method = 'avg'
        condition = ''
        result = self.avg.run(value,method,condition)
        self.assertEqual(result,2.5)

    def test_avg_empty_list(self):
        value = []
        method = 'avg'
        condition = ''
        with self.assertRaises(ZeroDivisionError):
            self.avg.run(value, method, condition)

    def test_avg_negative_numbers(self):
        value = [-5, 0, 5]
        method = 'avg'
        condition = ''
        result = self.avg.run(value, method, condition)
        self.assertEqual(result, 0)
    def test_avg_large_list(self):
        value = list(range(1, 10001))
        method = 'avg'
        condition = ''
        result = self.avg.run(value, method, condition)
        self.assertEqual(result, 5000.5)
    def test_avg_non_numeric_elements(self):
        value = [1, 'hello', 3.5, 'world']
        method = 'avg'
        condition = ''
        with self.assertRaises(TypeError):
            self.avg.run(value, method, condition)
    def test_avg_custom_condition(self):
        value = [1, 2, 3, 4, 5]
        method = 'avg'
        condition = '(x)=> x%2==0' # Only consider even numbers for average calculation.
        result = self.avg.run(value, method, condition)
        self.assertEqual(result, 3)  # The average of [2, 4] is 3.
    def test_avg_single_element_list(self):
        value = [10]
        method = 'avg'
        condition = ''
        result = self.avg.run(value, method, condition)
        self.assertEqual(result, 10)

if __name__=='__main__':
    unittest.main()