from sk_report_generator.reporter.script_evaluate.script_process import ScriptPrintProcess
from sk_report_generator.reporter.script_evaluate.script_process import ScriptProcess
import unittest

class TestScriptPrintProcess(unittest.TestCase):

    def setUp(self):
        self.script_process = ScriptProcess()
##        self.script_process=ScriptPrintProcess()

    def ntest_script_process(self):
        row_script = '''
for i in range(1,100):
    <<{i}>>

        '''
        template_script= '''<>
for i in range(1,100):
    <<{i}>>
        </>
        '''
        scripts = (template_script,row_script)

        result = self.script_process.run(scripts)
        print(result)

if __name__=='__main__':
    unittest.main()