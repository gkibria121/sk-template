from sk_report_generator.reporter.function_solver.function.sum import Sum
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestSnakeCase(unittest.TestCase):

    def setUp(self):
        self.sum = Sum()
        self.sum.set_next(MethodDefault())


    def test_snake_case(self):
        value = [1,2,3,4]
        method = 'sum'
        condition = ''
        result = self.sum.run(value, method, condition)
        self.assertEqual(result, 10)


    def test_sum_empty_list(self):
        value = []
        method = 'sum'
        condition = ''

        result = self.sum.run(value, method, condition)
        self.assertEqual(result,0)

    def test_sum_negative_numbers(self):
        value = [-5, 0, 5]
        method = 'sum'
        condition = ''
        result = self.sum.run(value, method, condition)
        self.assertEqual(result, 0)
    def test_sum_large_list(self):
        value = list(range(1, 10001))
        method = 'sum'
        condition = ''
        result = self.sum.run(value, method, condition)
        self.assertEqual(result, 50005000)
    def test_sum_non_numeric_elements(self):
        value = [1, 'hello', 3.5, 'world']
        method = 'sum'
        condition = ''
        with self.assertRaises(TypeError):
            self.sum.run(value, method, condition)
    def test_sum_custom_condition(self):
        value = [1, 2, 3, 4, 5]
        method = 'sum'
        condition = '(x)=> x%2==0' # Only consider even numbers for average calculation.
        result = self.sum.run(value, method, condition)
        self.assertEqual(result, 6)  # The average of [2, 4] is 3.
    def test_sum_single_element_list(self):
        value = [10]
        method = 'sum'
        condition = ''
        result = self.sum.run(value, method, condition)
        self.assertEqual(result, 10)

if __name__=='__main__':
    unittest.main()