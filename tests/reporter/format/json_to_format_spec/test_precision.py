import unittest
from sk_report_generator.reporter.formatter.json_to_format_spec.precision import PrecisionHandler
from sk_report_generator.reporter.formatter.json_to_format_spec.dufault import DefaultFormat


class TestAlign(unittest.TestCase):

    def setUp(self):
        self.align = PrecisionHandler()
        self.defualt =DefaultFormat()
        self.align.set_successor(self.defualt)

    def test_align(self):

        format_specs ={'precision' : '.1'}
        format_pattern = '{value:{precision}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:.1}')
        self.assertEqual(result[1],{})

        format_specs ={'precision' : '.2'}
        format_pattern = '{value:{precision}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:.2}')
        self.assertEqual(result[1],{})

        format_specs ={'precision' : '1'}
        format_pattern = '{value:{precision}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:1}')
        self.assertEqual(result[1],{})

        format_specs ={}
        format_pattern = '{value:{precision}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:}')
        self.assertEqual(result[1],{})

        format_specs ={'something' : ''}
        format_pattern = '{value:{precision}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:}')
        self.assertEqual(result[1],{'something' : ''})


if __name__ == '__main__':
    unittest.main()