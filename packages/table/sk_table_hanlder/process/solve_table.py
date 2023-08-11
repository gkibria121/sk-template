
class SolveTable:
    def __init__(self):
        self.single_table_solver =None
    def run(self,variable_tokens):
        temp_data = {}

        for variable in variable_tokens:
            if '$' not in variable[1]:
                temp_data.update({variable[0]: eval(variable[1])})
            else:
                value =self.single_table_solver.run(temp_data,variable)
                temp_data.update({variable[0] : value} )

        return temp_data

    def set_single_table_solver(self,solver):

        self.single_table_solver = solver
