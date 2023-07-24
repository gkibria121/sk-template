import unittest
from sk_report_generator.reporter.formatter.process.template_to_format_list import TemplateToFormatList


class TestTemplateToFormatList(unittest.TestCase):

    def setUp(self):
        self.template_to_format_list = TemplateToFormatList()

    def test_align(self):

        template = "<format>\ncustomAutoClass0 = {'width' : 1}</format>"
        result = self.template_to_format_list.run(template)
        self.assertEqual(result,{'customAutoClass0' :{'width' : 1} })

        template = "<format>\ncustomAutoClass0 ={'width' : 1,'align' : 'center'}</format>}"
        result = self.template_to_format_list.run(template)
        self.assertEqual(result,{'customAutoClass0' :{'width' : 1,'align' : 'center'} })

        template = "<format>\ncustomAutoClass0 ={'width' : 1,'align' : 'center'} \ncustomAutoClass1 ={'width' : 1,'align' : 'center'}\ncustomAutoClass2 ={'width' : 1,'align' : 'center'}\ncustomAutoClass3 ={'width' : 1,'align' : 'center'}\ncustomAutoClass4 ={'width' : 1,'align' : 'center'}\ncustomAutoClass4 ={'width' : 1,'align' : 'center'}</format>}"
        result = self.template_to_format_list.run(template)
        self.assertEqual(result,{'customAutoClass0' :{'width' : 1,'align' : 'center'},'customAutoClass1' :{'width' : 1,'align' : 'center'},'customAutoClass2' :{'width' : 1,'align' : 'center'},'customAutoClass3' :{'width' : 1,'align' : 'center'},'customAutoClass4' :{'width' : 1,'align' : 'center'} })
if __name__ == '__main__':
    unittest.main()