import unittest

from sk_report_generator.reporter.formatter.process.get_format_specs import GetFormatSpecs


class TestGetFormatSpecs(unittest.TestCase):

    def setUp(self):
        self.get_format_specs = GetFormatSpecs()

    def test_align(self):

        format_spec ='((x)=>x>1),c2'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list)
        self.assertEqual(result,{'width' : 10})

        format_spec ='((x)=>x>1)'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list)
        self.assertEqual(result,{})

        format_spec ='c2,c1'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list)
        self.assertEqual(result,{'width' : 10, 'align' : 'left'})

if __name__ == '__main__':
    unittest.main()