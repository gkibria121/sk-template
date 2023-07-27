from sk_report_generator.reporter.script_evaluate.script_process import ScriptPrintProcess
from sk_report_generator.reporter.script_evaluate.script_process import ScriptProcess
from sk_report_generator.reporter.default import Default
import unittest

class TestScriptPrintProcess(unittest.TestCase):

    def setUp(self):
        self.script_print_process = ScriptPrintProcess()
    def test_script_process(self):
        code = '{item.name}'
        result = self.script_print_process.process_code(code)
        self.assertEqual(result,'{item["name"]}')

        code = '{item.age}'
        result = self.script_print_process.process_code(code)
        self.assertEqual(result,'{item["age"]}')

        code = '{item.job}'
        result = self.script_print_process.process_code(code)
        self.assertEqual(result,'{item["job"]}')

        code = '{item.job.name}'
        result = self.script_print_process.process_code(code)
        self.assertEqual(result,'{item["job"]["name"]}')

        code = '{item.job.name[0]}'
        result = self.script_print_process.process_code(code)
        self.assertEqual(result,'{item["job"]["name"][0]}')

        code = '{item.job.name[0].salary}'
        result = self.script_print_process.process_code(code)
        self.assertEqual(result,'{item["job"]["name"][0]["salary"]}')

class TestScriptProcess(unittest.TestCase):

    def setUp(self):
        self.script_process = ScriptProcess()
        self.script_process.set_script_print_process(ScriptPrintProcess())
        self.default = type('MyClass', (object,), {'report': lambda script: script,'run' : lambda script: script})
        self.script_process.set_succesor(self.default)
        self.script_process.set_next(self.default)

    def test_script_process(self):
        template_script = '<>\nfor i in range(10):\n    <<{i}>><>'
        row_script = '\nfor i in range(10):\n    <<{i}>>'
        scripts = (template_script,row_script)
        result = self.script_process.run(scripts)
        self.assertEqual(result,('<>\nfor i in range(10):\n    <<{i}>><>',"\nfor i in range(10):\n    print(f'{i}')"))

        template_script = '<>\nfor i in range(10):\n    <<{i.name}>><>'
        row_script = '\nfor i in range(10):\n    <<{i.name}>>'
        scripts = (template_script,row_script)
        result = self.script_process.run(scripts)
        self.assertEqual(result,('<>\nfor i in range(10):\n    <<{i.name}>><>',"\nfor i in range(10):\n    print(f'{i[\"name\"]}')"))

        template_script = '<>\nfor i in range(10):\n    <<{i.name.id}>><>'
        row_script = '\nfor i in range(10):\n    <<{i.name.id}>>'
        scripts = (template_script,row_script)
        result = self.script_process.run(scripts)
        self.assertEqual(result,('<>\nfor i in range(10):\n    <<{i.name.id}>><>',"\nfor i in range(10):\n    print(f'{i[\"name\"][\"id\"]}')"))



if __name__=='__main__':
    unittest.main()