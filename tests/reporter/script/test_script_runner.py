from sk_report_generator.reporter.script_evaluate.script_runner import ScriptRunner
import unittest

class TestScriptRunner(unittest.TestCase):

    def setUp(self):
        self.script_runner = ScriptRunner()

    def test_script_replacer_single_line_script(self):
        # Test running a single-line script
        template_script = '<<print("Hello, world!")>>'
        row_script = 'print("Hello, world!")'
        scripts = (template_script, row_script)
        result = self.script_runner.run(scripts)
        self.assertEqual(result, (template_script, 'Hello, world!\n'))

    def test_script_replacer_multiline_script(self):
        # Test running a multi-line script
        template_script = '<<for i in range(3):\n    print(i)>>'
        row_script = 'for i in range(3):\n    print(i)'
        scripts = (template_script, row_script)
        result = self.script_runner.run(scripts)
        expected_output = '0\n1\n2\n'
        self.assertEqual(result, (template_script, expected_output))

    def test_script_replacer_syntax_error(self):
        # Test a script with syntax error
        template_script = '<<print("Hello, world!")>>'
        row_script = 'prnt("Hello, world!")'
        scripts = (template_script, row_script)
        with self.assertRaises(NameError):
            self.script_runner.run(scripts)

    def test_script_replacer_long_running_script(self):
        # Test a long-running script
        template_script = '<<import time\nfor i in range(5):\n    time.sleep(1)\n    print(i)>>'
        row_script = 'import time\nfor i in range(5):\n    time.sleep(1)\n    print(i)'
        scripts = (template_script, row_script)
        result = self.script_runner.run(scripts)
        expected_output = '0\n1\n2\n3\n4\n'
        self.assertEqual(result, (template_script, expected_output))

if __name__ == '__main__':
    unittest.main()
