import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.bool import Bool
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat




class TestBool(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.bool = Bool()
        self.bool.set_successor(self.default)

    def test_floor(self):
        value = 'True'
        format_spec =  {'bool' : 'yes|no'}

        result = self.bool.format(value,format_spec)
        self.assertEqual(result, 'yes')



if __name__ == "__main__":
    unittest.main()