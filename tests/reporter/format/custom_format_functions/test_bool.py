import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.bool import Bool
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat



class TestBool(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.bool = Bool()
        self.bool.set_successor(self.default)

    def test_yes_no(self):
        value = 'True'
        format_spec =  {'bool' : 'yes|no'}

        result = self.bool.format(value,format_spec)
        self.assertEqual(result, 'yes')

        value = 'False'
        result = self.bool.format(value,format_spec)
        self.assertEqual(result, 'no')
    def test_available_not_available(self):

        value = 'True'
        format_spec =  {'bool' : 'available|not available'}

        result = self.bool.format(value,format_spec)
        self.assertEqual(result, 'available')

        value = 'False'
        result = self.bool.format(value,format_spec)
        self.assertEqual(result, 'not available')

    def test_text(self):

        value = 'True'
        format_spec =  {'bool' : 'you are right|you are not right'}

        result = self.bool.format(value,format_spec)
        self.assertEqual(result, 'you are right')

        value = 'False'
        result = self.bool.format(value,format_spec)
        self.assertEqual(result, 'you are not right')
if __name__ == "__main__":
    unittest.main()
