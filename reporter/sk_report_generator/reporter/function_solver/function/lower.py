from .modules.check_condition import CheckCondition
import regex as re
import math



class LowerCase:
    def __init__(self):
        self.check_condition = CheckCondition()
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='lower':

            if condition =='':
                value =value.lower()
            if condition!='':
                if self.check_condition.run(value,condition):
                    value = value.lower()

        return self.go_next.run(value,method,condition)