import unittest
from sk_report_generator.reporter.formatter.json_to_format_spec.type import TypeHandler
from sk_report_generator.reporter.formatter.json_to_format_spec.dufault import DefaultFormat


class TestAlign(unittest.TestCase):

    def setUp(self):
        self.align = TypeHandler()
        self.defualt =DefaultFormat()
        self.align.set_successor(self.defualt)

    def test_align(self):

        format_specs ={'base' : 'b'}
        format_pattern = '{value:{base}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:b}')
        self.assertEqual(result[1],{})

        format_specs ={'base' : 'c'}
        format_pattern = '{value:{base}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:c}')
        self.assertEqual(result[1],{})

        format_specs ={'base' : 'e'}
        format_pattern = '{value:{base}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:e}')
        self.assertEqual(result[1],{})

        format_specs ={'base' : 'd'}
        format_pattern = '{value:{base}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:d}')
        self.assertEqual(result[1],{})

        format_specs ={}
        format_pattern = '{value:{base}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:}')
        self.assertEqual(result[1],{})

        format_specs ={'something' : ''}
        format_pattern = '{value:{base}}'
        result = self.align.handle(format_specs,format_pattern)
        self.assertEqual(result[0],'{value:}')
        self.assertEqual(result[1],{'something' : ''})

if __name__ == '__main__':
    unittest.main()