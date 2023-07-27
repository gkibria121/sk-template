from sk_report_generator.reporter.script_evaluate.script_replacer import ScriptReplacer
import unittest


class TestScriptReplacer(unittest.TestCase):

    def setUp(self):
        self.script_replacer = ScriptReplacer()

    def test_script_replacer(self):
        template ='<>\nfor i in range(10):\n    <<{i}>><>'
        template_script = '<>\nfor i in range(10):\n    <<{i}>><>'
        row_script = '\nfor i in range(10):\n    <<{i}>>'
        scripts = [(template_script,row_script)]
        result = self.script_replacer.run(template,scripts)
        self.assertEqual(result,'\nfor i in range(10):\n    <<{i}>>')

        template ='<>i am not procesed<>, i am out of script'
        template_script = '<>i am not procesed<>'
        row_script = 'I am processed'
        scripts = [(template_script,row_script)]
        result = self.script_replacer.run(template,scripts)
        self.assertEqual(result,'I am processed, i am out of script')
    def test_script_replacer_basic(self):
        # Test basic script replacement
        template = '<<Replace Me>>'
        template_script = '<<Replace Me>>'
        row_script = 'I am replaced!'
        scripts = [(template_script, row_script)]
        result = self.script_replacer.run(template, scripts)
        self.assertEqual(result, 'I am replaced!')

    def test_script_replacer_multiple_occurrences(self):
        # Test script replacement with multiple occurrences in the template
        template = '<<Replace Me>> and <<Replace Me>>'
        template_script = '<<Replace Me>>'
        row_script = 'I am replaced!'
        scripts = [(template_script, row_script)]
        result = self.script_replacer.run(template, scripts)
        self.assertEqual(result, 'I am replaced! and I am replaced!')

    def test_script_replacer_no_match(self):
        # Test when the template script is not found in the template
        template = 'This is a template without script'
        template_script = '<<Replace Me>>'
        row_script = 'I am replaced!'
        scripts = [(template_script, row_script)]
        result = self.script_replacer.run(template, scripts)
        self.assertEqual(result, template)



if __name__=='__main__':
    unittest.main()