import unittest
from sk_report_generator.reporter.function_solver.function.capitalize import Capitalize
from sk_report_generator.reporter.function_solver.function.default import MethodDefault

class TestCapitalize(unittest.TestCase):

    def setUp(self):
        self.capitalize = Capitalize()
        self.capitalize.set_next(MethodDefault())

    def test_capitalize_case(self):
        value = 'my name is gkibria'
        method = 'capitalize'
        condition = ''
        result = self.capitalize.run(value, method, condition)
        self.assertEqual(result, 'My Name Is Gkibria')

    def test_capitalize_empty_string(self):
        value = ''
        method = 'capitalize'
        condition = ''
        result = self.capitalize.run(value, method, condition)
        self.assertEqual(result, '')  # Or any other expected behavior for an empty string.

    def test_capitalize_all_uppercase(self):
        value = 'HELLO WORLD'
        method = 'capitalize'
        condition = ''
        result = self.capitalize.run(value, method, condition)
        self.assertEqual(result, 'Hello World')

    def test_capitalize_with_numbers(self):
        value = 'python3_example_123'
        method = 'capitalize'
        condition = ''
        result = self.capitalize.run(value, method, condition)
        self.assertEqual(result, 'Python3_example_123')

    def test_capitalize_with_special_characters(self):
        value = 'hello_world!how-are.you'
        method = 'capitalize'
        condition = ''
        result = self.capitalize.run(value, method, condition)
        self.assertEqual(result, 'Hello_world!How-Are.You')

    def test_capitalize_custom_condition(self):
        value = 'this is a test sentence with some unwanted words'
        method = 'capitalize'
        condition = '(x)=> "gkibria" not in x'
        result = self.capitalize.run(value, method, condition)
        self.assertEqual(result, 'This Is A Test Sentence With Some Unwanted Words')

    def test_capitalize_single_word(self):
        value = 'hello'
        method = 'capitalize'
        condition = ''
        result = self.capitalize.run(value, method, condition)
        self.assertEqual(result, 'Hello')


if __name__ == '__main__':
    unittest.main()
