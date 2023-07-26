from sk_report_generator.reporter.function_solver.function.snake import SnakeCase
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestSnakeCase(unittest.TestCase):

    def setUp(self):
        self.snake = SnakeCase()
        self.snake.set_next(MethodDefault())


    def test_snake_case(self):
        value = 'my name is gkibria'
        method = 'snake'
        condition = ''
        result = self.snake.run(value, method, condition)
        self.assertEqual(result, 'my_name_is_gkibria')

    def test_snake_case_all_uppercase(self):
        value = 'HELLO_WORLD'
        method = 'snake'
        condition = ''
        result = self.snake.run(value, method, condition)
        self.assertEqual(result, 'hello_world')
    def test_snake_case_mixed_case(self):
        value = 'HelloWorld'
        method = 'snake'
        condition = ''
        result = self.snake.run(value, method, condition)
        self.assertEqual(result, 'hello_world')
    def test_snake_case_with_spaces(self):
        value = '  hello world  '
        method = 'snake'
        condition = ''
        result = self.snake.run(value, method, condition)
        self.assertEqual(result, 'hello_world')

    def test_snake_case_empty_string(self):
        value = ''
        method = 'snake'
        condition = ''
        result = self.snake.run(value, method, condition)
        self.assertEqual(result, '')
    def test_snake_case_multiple_consecutive_spaces(self):
        value = 'hello   world'
        method = 'snake'
        condition = ''
        result = self.snake.run(value, method, condition)
        self.assertEqual(result, 'hello_world')

if __name__=='__main__':
    unittest.main()