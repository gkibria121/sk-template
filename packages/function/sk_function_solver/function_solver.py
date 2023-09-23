import regex as re
from .process_function_calling import ProcessFunctionCalling
from .single_function_solver import SingleFunctionSOlver
from .get_index_value import GetIndexValue
from .process_condition import ProcessCondition
class FunctionSolver:
    def __init__(self):
        self.obj = None
        self.obj_name = None
        self.data = None
        self.process_function_calling = ProcessFunctionCalling()
        self.single_obj_solver = SingleFunctionSOlver()
        self.single_obj_solver.set_get_index_value(GetIndexValue())
        self.single_obj_solver.set_process_condition(ProcessCondition())

    def solve(self, function_calling):

        function_calling = self.process_function_calling.run(function_calling)
        single_object_pattern = r'((\$\w+)((?:\.\w+(\(((?:[^()])|(?4))*\)))|(?:(?:\[\W?\w+\W?\])+))*)'
        single_boject_list = re.findall(single_object_pattern, function_calling)

        for single_object in single_boject_list:

            reslut = self.single_obj_solver.run(single_object[1],single_object[0])

            function_calling = re.sub(re.escape(single_object[0]) + r'(?=\s|\b|$)', str(reslut), function_calling)

        result = function_calling
        return result

    def set_data(self, data):
        self.data = data
        self.single_obj_solver.set_data(data)

    def create(self,function_name,argument,code):
        code = self.process_function_calling.run(code)
        self.single_obj_solver.def_function(function_name,argument,code)
        return ''

    def unittest(self,function_name,argument,list_of_test):
        result = self.single_obj_solver.unittest(function_name,argument,list_of_test)
        return result


    def set_ds_solver_chain(self,chain):
        self.ds_solver_chain = chain
        self.single_obj_solver.set_ds_solver_chain(self.ds_solver_chain)




