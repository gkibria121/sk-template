##import unittest
##from sk_report_generator.reporter.formatter.custom_format_functions.currency import Currency
##from sk_report_generator.reporter.formatter.custom_format_functions.currency import USD
##from sk_report_generator.reporter.formatter.custom_format_functions.currency import BDT
##from sk_report_generator.reporter.formatter.custom_format_functions.currency import GetBDTFormat
##from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat
##
##
##
##
##class TestCurrency(unittest.TestCase):
##
##    def setUp(self):
##        self.default = DefaultCustomFormat()
##        self.currency = Currency()
##        self.usd = USD()
##        self.bdt = BDT()
##        self.bdt.set_next(self.usd)
##        self.usd.set_next(self.default)
##
##    def test_floor(self):
##        value = 'True'
##        format_spec =  {'bool' : 'yes|no'}
##
##        result = self.bool.format(value,format_spec)
##        self.assertEqual(result, 'yes')
##
##
##
##if __name__ == "__main__":
##    unittest.main()