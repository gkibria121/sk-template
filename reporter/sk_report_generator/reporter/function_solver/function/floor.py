import regex as re
import math
from .modules.get_arg import GetArg
from .modules.check_condition import CheckCondition


class Floor:
    def set_next(self,go_next):
        self.go_next = go_next

    def __init__(self):
        self.get_floor = GetFloor()
        self.get_significance = GetArg()
        self.check_condition = CheckCondition()

    def run(self,value,method,condition):


        if method =='floor':

            if condition =='':
                value =math.floor(value)/1.0
            if condition !='':
                if self.check_condition.run(value,condition):
                    significance = self.get_significance.run(condition)
                    value = self.get_floor.run(value,significance)


        return self.go_next.run(value,method,condition)




class GetFloor:

    def run(self,value,significance):

        significance = float(significance)
        value = float(value)
        mod = value % significance

        if mod == 0:
            value = float(value)
        else:
            value = float(value- mod)
        return value
