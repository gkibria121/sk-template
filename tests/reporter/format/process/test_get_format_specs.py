import unittest

from sk_report_generator.reporter.formatter.process.get_format_specs import GetFormatSpecs


class TestGetFormatSpecs(unittest.TestCase):

    def setUp(self):
        self.get_format_specs = GetFormatSpecs()

    def test_format_spec_true(self):
        condition = True
        format_spec ='((x)=>x>1),c2'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{'width' : 10})

        format_spec ='((x)=>x>1)'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{})

        format_spec ='c2,c1'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{'width' : 10, 'align' : 'left'})

    def test_format_spec_false(self):
        condition = False
        format_spec ='((x)=>x>1),c2'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{})

        format_spec ='((x)=>x>1)'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{})

        format_spec ='c2,c1'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{})

    def test_or_class_true(self):
        condition = True
        format_spec ='((x)=>x>1),c1|c2'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{'align' : 'left'})


        format_spec ='((x)=>x>1),c1,c2|c3'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'},'c3' : {'width' : 13}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{'width' : 10,'align' : 'left'})

    def test_or_class_False(self):
        condition = False
        format_spec ='((x)=>x>1),c1|c2'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{'width' : 10})


        format_spec ='((x)=>x>1),c1,c2|c3'
        format_class_list = {'c2' : {'width' : 10},'c1': {'align' : 'left'},'c3' : {'width' : 13}}
        result = self.get_format_specs.run(format_spec,format_class_list,condition)
        self.assertEqual(result,{'width' : 13})

if __name__ == '__main__':
    unittest.main()