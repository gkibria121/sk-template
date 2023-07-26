from sk_report_generator.reporter.function_solver.function.set import Set
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestSet(unittest.TestCase):

    def setUp(self):
        self.set = Set()
        self.set.set_next(MethodDefault())

    def test_set(self):
        value = [1,2,3,4]
        method = 'set'
        condition = ''
        result = self.set.run(value,method,condition)
        self.assertEqual(result,{1, 2, 3, 4})
    def test_set_empty_list(self):
        value = []
        method = 'set'
        condition = ''
        result = self.set.run(value, method, condition)
        self.assertEqual(result, set())
    def test_set_with_duplicates(self):
        value = [1, 2, 3, 2, 4, 3, 1]
        method = 'set'
        condition = ''
        result = self.set.run(value, method, condition)
        self.assertEqual(result, {1, 2, 3, 4})
    def test_set_mixed_data_types(self):
        value = [1, 'hello', 3.14, 'world']
        method = 'set'
        condition = ''
        result = self.set.run(value, method, condition)
        self.assertEqual(result,{1, 'hello', 3.14, 'world'})
    def test_set_string(self):
        value = 'Hello, world!'
        method = 'set'
        condition = ''
        result = self.set.run(value, method, condition)
        self.assertEqual(result, {'H', 'e', 'l', 'o', ',', ' ', 'w', 'r', 'd', '!'})

    def test_set_list_with_emoji(self):
        value = ['😀', '🚀', '🌟', '😀']
        method = 'set'
        condition = ''
        result = self.set.run(value, method, condition)
        self.assertEqual(result, {'😀', '🚀', '🌟'})

if __name__=='__main__':
    unittest.main()