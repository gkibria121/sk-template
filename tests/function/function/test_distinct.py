from sk_function_solver.function.distinct import Distinct
from sk_function_solver.function.default import MethodDefault
import unittest

class TestAvg(unittest.TestCase):

    def setUp(self):
        self.distinct = Distinct()
        self.distinct.set_next(MethodDefault())
    def test_distinct(self):

        result = self.distinct.run([1,2,3,4,3,2,1],'distinct','(x)=> 2 in x')

        self.assertEqual(result,[1, 2, 3, 4])

    def test_distinct_all_distinct_elements(self):
        values = [1, 2, 3, 4, 5, 6]
        result = self.distinct.run(values, 'distinct', '')
        self.assertEqual(result, [1, 2, 3, 4, 5, 6])
    def test_distinct_with_duplicates(self):
        values = [1, 2, 3, 2, 4, 3, 1]
        result = self.distinct.run(values, 'distinct', '')
        self.assertEqual(result, [1, 2, 3, 4])
    def test_distinct_empty_list(self):
        values = []
        result = self.distinct.run(values, 'distinct', '')
        self.assertEqual(result, [])
    def test_distinct_mixed_data_types(self):
        values = [1, 'hello', 3.14, 'world', 1, 3.14]
        result = self.distinct.run(values, 'distinct', '')
        self.assertEqual(len(result),len( ['world', 1, 3.14, 'hello']))
    def test_distinct_single_element_list(self):
        values = [42]
        result = self.distinct.run(values, 'distinct', '')
        self.assertEqual(result, [42])
    def test_distinct_non_numeric_elements(self):
        values = ['apple', 'banana', 'orange', 'apple', 'grape']
        result = self.distinct.run(values, 'distinct', '')
        self.assertEqual(len(result), len(['grape', 'banana', 'apple', 'orange']))


if __name__ == '__main__':
    unittest.main()