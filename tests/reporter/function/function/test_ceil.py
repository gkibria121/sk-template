import unittest
from sk_report_generator.reporter.function_solver.function.ceil import Ceil
from sk_report_generator.reporter.function_solver.function.default import MethodDefault

class TestCeil(unittest.TestCase):

    def setUp(self):
        self.ceil = Ceil()
        self.ceil.set_next(MethodDefault())

    def test_ceil(self):
        value = 3.9
        method = 'ceil'
        condition = '(x)=>x>1,1'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '4.0')

        method = 'ceil'
        condition = '(x)=>x>5,1'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '3.9')


        value = 3.9
        method = 'ceil'
        condition = '5'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '5.0')
    def test_ceil_integer_value(self):
        value = 5
        method = 'ceil'
        condition = '5'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '5.0')

        value = 5.1
        method = 'ceil'
        condition = '0.5'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '5.5')

    def test_ceil_negative_value(self):
        value = -2.5
        method = 'ceil'
        condition = ''
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '-2.0')

    def test_ceil_zero(self):
        value = 0
        method = 'ceil'
        condition = ''
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '0.0')

    def test_ceil_large_value(self):
        value = 9999999.1
        method = 'ceil'
        condition = ''
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '10000000.0')

    def test_ceil_custom_condition(self):
        value = 5.5
        method = 'ceil'
        condition = '1'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '6.0')

    def test_ceil_custom_condition_round_up(self):
        value = -5.5
        method = 'ceil'
        condition = '1'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, '-5.0')

if __name__ == '__main__':
    unittest.main()
