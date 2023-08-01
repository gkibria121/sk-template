from ...controller.base import IFunction
import math


class CustomFunction(IFunction):

    def __init__(self):
        self.functions =['c1','c2','c3']


    def evaluate(self,match):
        if match[0] in self.functions:
            try:
                function = f'{match[0]}'
                value = f'{match[1]}'
                exec(self.scripts)
                result = eval(f'{function}({value})')
                return result
            except NameError:
                self.error_handler.set_error(f'Syntax Error: Function is not defined {match[0]}()')

        if(self.error_handler.get_error()):
            return self.error_handler.get_error()

        return self.successor.evaluate(match)



    def set_successor(self,successor):

        self.successor  = successor

    def set_error_handler(self,handler):
        self.error_handler = handler

    def set_scripts(self,scripts):
        self.scripts = scripts
