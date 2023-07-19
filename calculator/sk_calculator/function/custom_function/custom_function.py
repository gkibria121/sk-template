from ...controller.base import IFunction
import math


class CustomFunction(IFunction):

    def __init__(self):
        self.functions =['c1','c2','c3']


    def evaluate(self,match):
        if match[0] in self.functions:
            try:
                function = eval(f'{match[0]}')
                value = eval(f'{match[1]}')
                result = function(value)
                return round(deg,9)
            except ValueError:
                self.error_handler.set_error(f'Math Error : Math Domain Error at {match[0]}({match[1]})')

        if(self.error_handler.get_error()):
            return self.error_handler.get_error()

        return self.successor.evaluate(match)



    def set_successor(self,successor):

        self.successor  = successor

    def set_error_handler(self,handler):
        self.error_handler = handler
