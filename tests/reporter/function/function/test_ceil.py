import unittest
from sk_report_generator.reporter.function_solver.function.ceil import Ceil
from sk_report_generator.reporter.function_solver.function.ceil import GetCeil
from sk_report_generator.reporter.function_solver.function.modules.get_arg import GetArg
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
        self.assertEqual(result, 4.0)

        method = 'ceil'
        condition = '(x)=>x>5,1'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, 3.9)


        value = 3.9
        method = 'ceil'
        condition = '5'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, 5.0)
    def test_ceil_integer_value(self):
        value = 5
        method = 'ceil'
        condition = '5'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, 5.0)

        value = 5.1
        method = 'ceil'
        condition = '0.5'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, 5.5)

    def test_ceil_negative_value(self):
        value = -2.5
        method = 'ceil'
        condition = ''
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, -2.0)

    def test_ceil_zero(self):
        value = 0
        method = 'ceil'
        condition = ''
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, 0.0)

    def test_ceil_large_value(self):
        value = 9999999.1
        method = 'ceil'
        condition = ''
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, 10000000.0)

    def test_ceil_custom_condition(self):
        value = 5.5
        method = 'ceil'
        condition = '1'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, 6.0)

    def test_ceil_custom_condition_round_up(self):
        value = -5.5
        method = 'ceil'
        condition = '1'
        result = self.ceil.run(value, method, condition)
        self.assertEqual(result, -5.0)


class TestGetCeil(unittest.TestCase):

    def setUp(self):
        self.get_ceil = GetCeil()

    def test_get_ceil(self):
        self.assertEqual(self.get_ceil.run(value=3.9, significance=1), 4.0)

    def test_get_ceil_positive_integer(self):
        self.assertEqual(self.get_ceil.run(value=5, significance=1), 5.0)

    def test_get_ceil_negative_float(self):
        self.assertEqual(self.get_ceil.run(value=-7.3, significance=0.5), -7.0)

    def test_get_ceil_zero(self):
        self.assertEqual(self.get_ceil.run(value=0, significance=2), 0.0)

    def test_get_ceil_large_values(self):
        self.assertEqual(self.get_ceil.run(value=10000, significance=1000), 10000.0)

    def test_get_ceil_small_values(self):
        self.assertEqual(self.get_ceil.run(value=0.0001, significance=0.00001), 0.0001)

    def test_get_ceil_negative_values(self):
        self.assertEqual(self.get_ceil.run(value=-2.8, significance=-1), -3.0)

    def test_get_ceil_non_numeric(self):
        with self.assertRaises(ValueError):
            self.get_ceil.run(value='abc', significance=1)

    def test_get_ceil_non_numeric_significance(self):
        with self.assertRaises(ValueError):
            self.get_ceil.run(value=7.5, significance='def')

    def test_get_ceil_large_float_result(self):
        self.assertEqual(self.get_ceil.run(value=999.999, significance=0.001), 1000.0)

    def test_get_ceil_zero_values(self):
        with self.assertRaises(ZeroDivisionError):
            self.get_ceil.run(value=0, significance=0)


class TestGetSignificance(unittest.TestCase):

    def setUp(self):
        self.get_significance = GetArg()

    def test_significance(self):

        self.assertEqual(self.get_significance.run('(x)=>x!=1,2'),'2')
        self.assertEqual(self.get_significance.run('(x)=>x!=1,1,2'),'1')

    def test_significance_no_condition(self):

        self.assertEqual(self.get_significance.run('2'),'2')


if __name__ == '__main__':
    unittest.main()

    unittest.main()
