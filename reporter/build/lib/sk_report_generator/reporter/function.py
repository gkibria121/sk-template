import regex as re
from .function_solver.function_solver import FunctionSolver
from .base import IReporter
from .function_solver.process_function_calling import ProcessFunctionCalling
from .function_solver.single_function_solver import SingleFunctionSOlver
from .function_solver.get_index_value import GetIndexValue
from .function_solver.process_condition import ProcessCondition
class FunctionEvaluator(IReporter):
    def __init__(self):
        self.successor = None
        self.data = None
        self.process_function_calling = ProcessFunctionCalling()
        self.single_function_solver = SingleFunctionSOlver()
        self.single_function_solver.set_get_index_value(GetIndexValue())
        self.single_function_solver.set_process_condition(ProcessCondition())
        self.function_solver = FunctionSolver()
        self.function_solver.set_process_function_calling(self.process_function_calling)
        self.function_solver.set_single_obj_solver(self.single_function_solver)

    def report(self, template):
        pattern = r'({({(?:((?:[^{}]|(?2))*?))(?:(?:\:[^{}\[\]]+)|((?:\:\:)(.*)))?})})'

        matches = re.findall(pattern, template)

        for match in matches:
            changed_value = match[0]
            result = self.function_solver.solve(match[2])
            changed_value = re.sub(re.escape(match[2]), result, changed_value)
            template = re.sub(re.escape(match[0]), changed_value, template)

        return self.successor.report(template)

    def set_successor(self, successor):
        self.successor = successor

    def set_data(self, data):
        self.data = data
        self.function_solver.set_data(self.data)
