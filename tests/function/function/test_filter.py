from sk_function_solver.function.filter import Filter
from sk_function_solver.function.default import MethodDefault
import unittest

class TestFilter(unittest.TestCase):

    def setUp(self):
        self.filter = Filter()
        self.filter.set_next(MethodDefault())

    def test_avg(self):
        value = [1,2,3,4]
        method = 'where'
        condition = '(x)=>x>1'
        result = self.filter.run(value,method,condition)
        self.assertEqual(result,[2, 3, 4])
    def test_filter_different_condition(self):
        value = [10, 20, 30, 40, 50]
        method = 'where'
        condition = '(x) => x < 40'
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, [10, 20, 30])

    def test_filter_with_negative_number(self):
        value = [-1, 0, 1, 2, 3]
        method = 'where'
        condition = '(x) => x >= 0'
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, [0, 1, 2, 3])
    def test_filter_empty_list(self):
        value = []
        method = 'where'
        condition = '(x) => x > 0'
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, [])
    def test_filter_with_strings(self):
        value = ['apple', 10, 'banana', 20, 'orange']
        method = 'where'
        condition = '(x) => type(x) == str'
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, ['apple', 'banana', 'orange'])
    def test_filter_empty_result(self):
        value = [1, 2, 3, 4, 5]
        method = 'where'
        condition = '(x) => x > 10'
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, [])
    def test_filter_all_meeting_condition(self):
        value = [5, 10, 15, 20, 25]
        method = 'where'
        condition = '(x) => x >= 5'
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, [5, 10, 15, 20, 25])


if __name__=='__main__':
    unittest.main()