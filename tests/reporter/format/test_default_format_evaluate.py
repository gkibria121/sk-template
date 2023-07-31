import unittest

from sk_report_generator.reporter.formatter.default_format_evaluate import DefaultFormat


class TestGetEvaluateDefaultFormat(unittest.TestCase):

    def setUp(self):
        self.default_format_evaluate = DefaultFormat()
        self.default_format_evaluate.go_next=type('default',(),{'run' : lambda value,format_spec,format_class_list: value})

    def test_format(self):

        value = '2'
        format_spec = '^30'
        result = self.default_format_evaluate.run(value,format_spec,format_class_list={})
        self.assertEqual(result,'              2               ')

        value = '2'
        format_spec = '#^30'
        result = self.default_format_evaluate.run(value,format_spec,format_class_list={})
        self.assertEqual(result,'##############2###############')
        value = 'gkibria'
        format_spec = '#^30'
        result = self.default_format_evaluate.run(value,format_spec,format_class_list={})
        self.assertEqual(result,'###########gkibria############')

    def test_format_with_long_value(self):
        value = 'This is a very long value that needs to be truncated'
        format_spec = '^30'
        result = self.default_format_evaluate.run(value, format_spec, format_class_list={})
        self.assertEqual(result, 'This is a very long value that needs to be truncated')

    def test_format_with_left_alignment(self):
        value = 'left'
        format_spec = '<15'
        result = self.default_format_evaluate.run(value, format_spec, format_class_list={})
        self.assertEqual(result, 'left           ')

    def test_format_with_right_alignment(self):
        value = 'right'
        format_spec = '>15'
        result = self.default_format_evaluate.run(value, format_spec, format_class_list={})
        self.assertEqual(result, '          right')

    def test_format_with_zero_padding(self):
        value = '7'
        format_spec = '06'
        result = self.default_format_evaluate.run(value, format_spec, format_class_list={})
        self.assertEqual(result, '000007')

    def test_format_with_decimal_precision(self):
        value = 123.456789
        format_spec = '.2f'
        result = self.default_format_evaluate.run(value, format_spec, format_class_list={})
        self.assertEqual(result, '123.46')

    def test_format_with_custom_special_character(self):
        value = 'hello'
        format_spec = '@^15'
        result = self.default_format_evaluate.run(value, format_spec, format_class_list={})
        self.assertEqual(result, '@@@@@hello@@@@@')

    def test_format_with_multiple_format_specifiers(self):
        value = 'hello'
        format_spec = '^15.10'
        result = self.default_format_evaluate.run(value, format_spec, format_class_list={})
        self.assertEqual(result, '     hello     ')

if __name__ == '__main__':
    unittest.main()