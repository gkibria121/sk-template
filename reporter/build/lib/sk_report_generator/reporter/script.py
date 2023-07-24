import regex as re
from .script_evaluate.script_runner import ScriptRunner
from .script_evaluate.script_replacer import ScriptReplacer
from .script_evaluate.script_process import ScriptProcess
from .base import IReporter


class ScriptEvaluator(IReporter):

    def __init__(self):
        self.successor = None
        self.data = None
        self.process = ScriptProcess()
        self.script_runner = ScriptRunner()
        self.script_replacer = ScriptReplacer()

        self.process.set_next(self.script_runner)

    def report(self, template):
        pattern = r'(\<\>([\s\S]*?)\<\/\>)'
        matches = re.findall(pattern, template)
        scripts = []
        for match in matches:
            script_result_tuple = self.process.run(match)
            scripts.append(script_result_tuple)

        template = self.script_replacer.run(template, scripts)

        return self.successor.report(template)

    def set_successor(self, successor):
        self.successor = successor
        self.process.set_succesor(successor)
        self.script_runner.set_succesor(successor)

    def set_data(self, data):
        self.data = data
