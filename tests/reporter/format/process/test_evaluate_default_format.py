import unittest

from sk_report_generator.reporter.formatter.process.evaluate_default_format import EvaluateDefaultFormat


class TestGetEvaluateDefaultFormat(unittest.TestCase):

    def setUp(self):
        self.evaluate_format_spec = EvaluateDefaultFormat()

    def test_format(self):

        value = 2
        format_pattern = 'b'
        result = self.evaluate_format_spec.run(value,format_pattern)
        self.assertEqual(result,'10')

        value = 1000000000.0
        format_pattern = 'e'
        result = self.evaluate_format_spec.run(value,format_pattern)
        self.assertEqual(result,'1.000000e+09')

        format_pattern = '.2e'
        result = self.evaluate_format_spec.run(value,format_pattern)
        self.assertEqual(result,'1.00e+09')

        value = 'gkibria'
        format_pattern = '$^30'
        result = self.evaluate_format_spec.run(value,format_pattern)
        self.assertEqual(result,'$$$$$$$$$$$gkibria$$$$$$$$$$$$')

      # Test integer formatting with different patterns
        value = 123456789
        format_pattern = 'd'
        result = self.evaluate_format_spec.run(value, format_pattern)
        self.assertEqual(result, '123456789')

        format_pattern = '10d'  # Test alignment
        result = self.evaluate_format_spec.run(value, format_pattern)
        self.assertEqual(result, ' 123456789')

        # Test float formatting
        value = 1234.5678
        format_pattern = '.3f'
        result = self.evaluate_format_spec.run(value, format_pattern)
        self.assertEqual(result, '1234.568')

        # Test string formatting
        value = 'hello'
        format_pattern = '>10'
        result = self.evaluate_format_spec.run(value, format_pattern)
        self.assertEqual(result, '     hello')

        format_pattern = '<10'  # Test left alignment
        result = self.evaluate_format_spec.run(value, format_pattern)
        self.assertEqual(result, 'hello     ')


if __name__ == '__main__':
    unittest.main()