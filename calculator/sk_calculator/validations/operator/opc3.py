from ...controller.base import IValidation
import regex
from ...controller.function import FunctionHandler
class Op3(IValidation):
    def __init__(self):
        self.function_handler = FunctionHandler()
        self.custom_function = self.function_handler.custom.functions
        self.valid_functions = [key for key, value in vars(self.function_handler).items() if '__' not in key]+self.custom_function

    def check_error(self,expression):


        ## missing operator between brackets and numbers

        operators_pattern = '(?<!\w)(\d+(?:\.\d+)?)\((\d+(?:\.\d+)?)'

        matches = regex.findall(operators_pattern,expression)

        if matches:
            for match in matches:
                self.error_handler.set_error('Syntax Error : Missing Operator '+match[1]+'?('+match[2])
        return self.successor.check_error(expression)



    def set_successor(self,successor):

        self.successor  = successor

    def set_error_handler(self,handler):
        self.error_handler = handler