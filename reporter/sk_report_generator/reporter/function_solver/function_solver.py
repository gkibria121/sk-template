import regex as re


class FunctionSolver:
    def __init__(self):
        self.obj = None
        self.obj_name = None
        self.data = None
        self.process_function_calling = None
        self.single_obj_solver = None

    def solve(self, function_calling):

        function_calling = self.process_function_calling.run(function_calling)
        single_object_pattern = r'((\$\w+)((?:\.\w+(\(((?:[^()])|(?4))*\)))|(?:(?:\[\W?\w+\W?\])+))*)'
        single_boject_list = re.findall(single_object_pattern, function_calling)

        for single_object in single_boject_list:

            reslut = self.single_obj_solver.run(single_object[1],single_object[2])

            function_calling = re.sub(re.escape(single_object[0]) + r'(?=\s|\b|$)', str(reslut), function_calling)

        result = function_calling
        return result

    def set_data(self, data):
        self.data = data
        self.single_obj_solver.set_data(data)

    def set_process_function_calling(self,process_function_calling):
        self.process_function_calling = process_function_calling

    def set_single_obj_solver(self,single_obj_solver):
        self.single_obj_solver = single_obj_solver







