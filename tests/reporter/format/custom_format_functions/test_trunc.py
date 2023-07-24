import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.trunc import Trunc
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat




class TestTrunc(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.trunc = Trunc()
        self.trunc.set_successor(self.default)

    def test_round(self):
        value = 100.999999
        format_spec =  {'trunc' : 2}

        result = self.trunc.format(value,format_spec)
        self.assertEqual(result, '100.99')

        value = 100.999999999
        format_spec =  {'trunc' : 5}

        result = self.trunc.format(value,format_spec)
        self.assertEqual(result, '100.99999')


        value = 100.999999999
        format_spec =  {'trunc' : 9}

        result = self.trunc.format(value,format_spec)
        self.assertEqual(result, '100.999999999')


        value = 100.999999999
        format_spec =  {'trunc' : 0}

        result = self.trunc.format(value,format_spec)
        self.assertEqual(result, '100.0')
if __name__ == "__main__":
    unittest.main()