from sk_report_generator.reporter.function_solver.function.reverse import Reverse
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestReverse(unittest.TestCase):

    def setUp(self):
        self.filter = Reverse()
        self.filter.set_next(MethodDefault())

    def test_reverse(self):
        value = [1,2,3,4]
        method = 'reverse'
        condition = '(x)=>x>1'
        result = self.filter.run(value,method,condition)
        self.assertEqual(result,[4, 3, 2])
    def test_reverse_empty_list(self):
        value = []
        method = 'reverse'
        condition = ''
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, [])
    def test_reverse_single_element_list(self):
        value = [42]
        method = 'reverse'
        condition = ''
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, [42])
    def test_reverse_with_duplicates(self):
        value = [1, 2, 3, 2, 4, 3, 1]
        method = 'reverse'
        condition = ''
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, [1, 3, 4, 2, 3, 2, 1])
    def test_reverse_mixed_data_types(self):
        value = [1, 'hello', 3.14, 'world']
        method = 'reverse'
        condition = ''
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, ['world', 3.14, 'hello', 1])
    def test_reverse_string(self):
        value = 'Hello, world!'
        method = 'reverse'
        condition = ''
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, '!dlrow ,olleH')
    def test_reverse_string_with_special_characters(self):
        value = '!@#$%^'
        method = 'reverse'
        condition = ''
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, "^%$#@!")
    def test_reverse_list_with_emoji(self):
        value = ['😀', '🚀', '🌟']
        method = 'reverse'
        condition = ''
        result = self.filter.run(value, method, condition)
        self.assertEqual(result, ['🌟', '🚀', '😀'])


if __name__=='__main__':
    unittest.main()