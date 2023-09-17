import regex as re
from sk_function_solver.function_solver import FunctionSolver
from .base import IReporter
from sk_function_solver.process_function_calling import ProcessFunctionCalling
from sk_function_solver.single_function_solver import SingleFunctionSOlver
from sk_function_solver.get_index_value import GetIndexValue
class FunctionEvaluator(IReporter):
    def __init__(self):
        self.successor = None
        self.data = None
        self.function_solver = None
    def report(self, template):
        pattern = r'(\{\{(?:[\"\']*)(((\{([^{}]|(?4))*\})|([^{}:]+))*)((\:([^{}:]+))|(\:\:(?4)))?(?:[\"\']*)\}\})'

        matches = re.findall(pattern, template)

        for match in matches:
            changed_value = match[0]
            result = self.function_solver.solve(match[1])
            changed_value = re.sub(re.escape(match[1]), result, changed_value)
            template = re.sub(re.escape(match[0]), changed_value, template)

        return self.successor.report(template)

    def set_function_solver(self,solver):
        self.function_solver = solver


    def set_successor(self, successor):
        self.successor = successor

    def set_data(self, data):
        self.data = data
        self.function_solver.set_data(self.data)
