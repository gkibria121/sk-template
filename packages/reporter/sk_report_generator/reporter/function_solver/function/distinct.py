from .modules.check_condition import CheckCondition
import regex as re
import math

class Distinct:
    def __init__(self):
        self.check_condition =CheckCondition()
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='distinct':

            if condition =='':
                value =list(set(value))
            if condition!='':
                if self.check_condition.run(value,condition):
                    value =list(set(value))



        return self.go_next.run(value,method,condition)