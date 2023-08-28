from .reporter.default import Default
from .reporter.format import Formatter
from .reporter.script import ScriptEvaluator
from .reporter.function import FunctionEvaluator
from .reporter.template.template_module import Moduler
from .reporter.operation import OperationHandler
import regex as re
from pathlib import Path
class ReportGenerator:

    def __init__(self):
        self.function_evaluate = FunctionEvaluator()
        self.script_evaluate = ScriptEvaluator()
        self.format = Formatter()
        self.operation = OperationHandler()
        self.default = Default()
        self.moduler = Moduler()
        self.moduler.set_successor(self.function_evaluate)
        self.function_evaluate.set_successor(self.script_evaluate)
        self.script_evaluate.set_successor(self.operation)
        self.operation.set_successor(self.format)
        self.format.set_successor(self.default)
        self.data = None

    def generate_report(self, template, data):
        self.set_data(data)
        result = self.moduler.report(template)
        return result

    def set_data(self, data):
        self.data = data
        self.function_evaluate.set_data(self.data)
        self.script_evaluate.set_data(self.data)
        self.format.set_data(self.data)
        self.function_evaluate.function_solver.single_obj_solver.foreach.set_data(self.data)

    def set_reporter(self,reporter):
        self.function_evaluate.function_solver.single_obj_solver.foreach.set_reporter(reporter)





