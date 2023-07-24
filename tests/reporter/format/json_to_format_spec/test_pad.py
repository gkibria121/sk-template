import unittest
from sk_report_generator.reporter.formatter.json_to_format_spec.pad import PadHandler
from sk_report_generator.reporter.formatter.json_to_format_spec.dufault import DefaultFormat


class TestAlign(unittest.TestCase):

    def setUp(self):
        self.align = PadHandler()
        self.defualt =DefaultFormat()
        self.align.set_successor(self.defualt)

    def test_align(self):

        format_specs ={'pad' : '#'}
        format_pattern = '{value:{pad}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:#}')
        self.assertEqual(result[1],{})
        format_specs ={}
        format_pattern = '{value:{pad}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:}')
        self.assertEqual(result[1],{})

        format_specs ={'something' : ''}
        format_pattern = '{value:{pad}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:}')
        self.assertEqual(result[1],{'something' : ''})


if __name__ == '__main__':
    unittest.main()