import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.ceil import Ceil
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat





class TestCeil(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.ceil = Ceil()
        self.ceil.set_successor(self.default)

    def test_ceil(self):
        value = '1.2'
        format_spec =  {'ceil' : True}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '2.0')

        value = '9.2'
        format_spec =  {'ceil' : True}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '10.0')

        value = '1000.2'
        format_spec =  {'ceil' : True}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '1001.0')

    def test_ceil_significance(self):
        value = '1.2'
        format_spec =  {'ceil-significance' : 1}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '2.0')

        value = '9.2'
        format_spec =  {'ceil-significance' : 2}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '10.0')

        value = '1000.2'
        format_spec =  {'ceil-significance' : 5}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '1005.0')

    def test_ceil_significance(self):
        value = '1.2'
        format_spec =  {'ceil-significance' : 0.2}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '1.2')

        value = '9.2'
        format_spec =  {'ceil-significance' : 0.2}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '9.2')

        value = '1000.2'
        format_spec =  {'ceil-significance' : 0.5}

        result = self.ceil.format(value,format_spec)
        self.assertEqual(result, '1000.5')

if __name__ == "__main__":
    unittest.main()