import unittest

from sk_report_generator.reporter.formatter.process.template_format_process import TemplateFormatProcess


class TestTemplateFormatProcess(unittest.TestCase):

    def setUp(self):
        self.template_format_process = TemplateFormatProcess()

    def test_align(self):

        template = "{{$x::{'width' : 1}}}"
        result = self.template_format_process.run(template)
        self.assertEqual(result,"{{$x:customAutoClass0}}<format>\ncustomAutoClass0 = {'width' : 1}</format>")


if __name__ == '__main__':
    unittest.main()