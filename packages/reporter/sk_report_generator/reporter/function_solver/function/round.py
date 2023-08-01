from .modules.check_condition import CheckCondition
from .modules.get_arg import GetArg
import regex as re
import math



class Round:
    def __init__(self):
        self.check_condition = CheckCondition()
        self.get_arg = GetArg()
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='round':

            if condition=='':
                value =round(value,9)

            if condition !='':
                if self.check_condition.run(value,condition):
                    condition = self.get_arg.run(condition)
                    value =round(value,int(condition))

        return self.go_next.run(value,method,condition)