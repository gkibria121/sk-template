import unittest
from sk_report_generator.reporter.formatter.custom_format_functions.round import Round
from sk_report_generator.reporter.formatter.custom_format_functions.default import DefaultCustomFormat




class TestRound(unittest.TestCase):

    def setUp(self):
        self.default = DefaultCustomFormat()
        self.round = Round()
        self.round.set_successor(self.default)

    def test_round(self):
        value = 100.999999
        format_spec =  {'round' : 2}

        result = self.round.format(value,format_spec)
        self.assertEqual(result, '101.0')

        value = 100.999999999
        format_spec =  {'round' : 5}

        result = self.round.format(value,format_spec)
        self.assertEqual(result, '101.0')


        value = 100.999999999
        format_spec =  {'round' : 9}

        result = self.round.format(value,format_spec)
        self.assertEqual(result, '100.999999999')

if __name__ == "__main__":
    unittest.main()