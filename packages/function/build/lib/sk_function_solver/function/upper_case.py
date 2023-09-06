from .modules.check_condition import CheckCondition
import regex as re
import math



class UpperCase:
    def __init__(self):
        self.check_condition = CheckCondition()
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='upper':

            if condition =='':
                value =value.upper()
            if condition!='':
                if self.check_condition.run(value,condition):
                    value = value.upper()

        return self.go_next.run(value,method,condition)