import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.str_continue import StrContinue
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat




class TestBool(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.str_continue = StrContinue()
        self.str_continue.set_successor(self.default)

    def test_continue(self):
        value = '123456789'
        format_spec = {'continue' : 5}

        expected_report ='12...'
        report =self.str_continue.format(value,format_spec)
        self.assertEqual(report,expected_report)

        format_spec = {'continue' : 2}

        expected_report ='12'
        report =self.str_continue.format(value,format_spec)
        self.assertEqual(report,expected_report)

        format_spec = {'continue' : 8}

        expected_report ='12345...'
        report =self.str_continue.format(value,format_spec)
        self.assertEqual(report,expected_report)
        format_spec = {'continue' : 13}

        expected_report ='123456789'
        report =self.str_continue.format(value,format_spec)
        self.assertEqual(report,expected_report)



        value = 'abcdefghijklmnopqrstwvxyzABCDEFGHIJKLMNOPQRSTWVXYZ'
        format_spec = {'continue' : 5}

        expected_report ='ab...'
        report =self.str_continue.format(value,format_spec)
        self.assertEqual(report,expected_report)

        value = 'abcdefghijklmnopqrstwvxyzABCDEFGHIJKLMNOPQRSTWVXYZ'
        format_spec = {'continue' : 10}

        expected_report ='abcdefg...'
        report =self.str_continue.format(value,format_spec)
        self.assertEqual(report,expected_report)
if __name__ == "__main__":
    unittest.main()