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


if __name__ == '__main__':
    unittest.main()