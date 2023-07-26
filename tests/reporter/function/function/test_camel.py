from sk_report_generator.reporter.function_solver.function.camel import CamelCase
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestAvg(unittest.TestCase):

    def setUp(self):
        self.camel = CamelCase()
        self.camel.set_next(MethodDefault())


    def test_camel_case(self):
        value = 'my name is gkibria'
        method = 'camel'
        condition = ''
        result = self.camel.run(value, method, condition)
        self.assertEqual(result, 'MyNameIsGkibria')

    def test_camel_case_empty_string(self):
        value = ''
        method = 'camel'
        condition = ''
        result = self.camel.run(value, method, condition)
        self.assertEqual(result, '')  # Or any other expected behavior for an empty string.

    def test_camel_case_all_uppercase(self):
        value = 'HELLO WORLD'
        method = 'camel'
        condition = ''
        result = self.camel.run(value, method, condition)
        self.assertEqual(result, 'HelloWorld')

    def test_camel_case_with_numbers(self):
        value = 'python3_example_123'
        method = 'camel'
        condition = ''
        result = self.camel.run(value, method, condition)
        self.assertEqual(result, 'Python3Example123')

    def test_camel_case_with_special_characters(self):
        value = 'hello_world!how-are.you'
        method = 'camel'
        condition = ''
        result = self.camel.run(value, method, condition)
        self.assertEqual(result, 'HelloWorldHowAreYou')

    def test_camel_case_custom_condition(self):
        value = 'this is a test sentence with some unwanted words'
        method = 'camel'
        condition = '(x)=> "gkibria" not in x'
        result = self.camel.run(value, method, condition)
        self.assertEqual(result, 'ThisIsATestSentenceWithSomeUnwantedWords')

    def test_camel_case_single_word(self):
        value = 'hello'
        method = 'camel'
        condition = ''
        result = self.camel.run(value, method, condition)
        self.assertEqual(result, 'Hello')
if __name__=='__main__':
    unittest.main()