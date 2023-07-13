import regex as re

from .single_function_solver import SingleFunctionSOlver

class FunctionSolver:
    def __init__(self):
        self.obj = None
        self.obj_name = None
        self.data = None

        self.process_function_calling = ProcessFunctionCalling()
        self.single_obj_solver = SingleFunctionSOlver()

    def solve(self, function_calling):

        function_calling = self.process_function_calling.run(function_calling)
        single_object_pattern = r'((\$\w+)((?:\.\w+(\(((?:[^()])|(?4))*\)))|(?:(?:\[\W?\w+\W?\])+))*)'
        single_boject_list = re.findall(single_object_pattern, function_calling)

        for single_object in single_boject_list:

            reslut = self.single_obj_solver.run(single_object)

            function_calling = re.sub(re.escape(single_object[0]) + r'(?=\s|\b|$)', str(reslut), function_calling)

        result = function_calling
        return result

    def set_data(self, data):
        self.data = data
        self.single_obj_solver.set_data(data)

    def get_obj(self, name):

        return self.data[name]



class ProcessFunctionCalling:
    def __init__(self):
        pass
    def run(self,function_calling):

        pattern = r'(?:(?<!:)(?:\.([^\W\d][\w]*))\b(?!\())'
        function_calling = re.sub(pattern, lambda match: f'["{match.group(1)}"]', function_calling)

        return function_calling





