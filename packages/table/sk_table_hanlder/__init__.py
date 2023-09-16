import regex as re
from .process.create_declaration_list import CreateDeclarationText
from .process.get_variable_tokens import GetVariableTokens
from .process.solve_table import SolveTable
from .process.single_table_solver import SingleTableSolver

class TableHandler:

    def __init__(self):
        self.data = {}
        self.wrapper = None
        self.monog_controller = None
        self.create_declaration_text = CreateDeclarationText()
        self.get_variable_tokens= GetVariableTokens()
        self.solve_table = SolveTable()
        self.single_table_solver = SingleTableSolver()
        self.solve_table.set_single_table_solver(self.single_table_solver)


    def process(self,variable_declarations):
        variable_tokens = self.get_variable_tokens.run(variable_declarations)

        declaration_list = self.solve_table.run(variable_tokens)
        declaration_text = self.create_declaration_text.run(declaration_list)

        return self.go_next.process(declaration_text)

    def set_wrapper(self,wrapper):
        self.wrapper = wrapper

        self.single_table_solver.set_wrapper(self.wrapper)

    def set_mongo_controller(self,controller):
        self.single_table_solver.set_mongo_controller(controller)
        self.monog_controller = controller


    def set_next(self,go_next):
        self.go_next = go_next


    def set_function_solver(self,solver):
        self.single_table_solver.set_function_solver(solver)



