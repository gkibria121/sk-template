import regex as re
import math

from .modules.get_arg import GetArg
from .modules.check_condition import CheckCondition
class Count:
    def __init__(self):
        self.get_item = GetArg()
        self.get_count = GetCount()
        self.check_condition = CheckCondition()


    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='count':

            if condition =='':
                value =0
            if condition !='':
                if self.check_condition.run(value,condition):
                    item = self.get_item.run(condition)
                    value = self.get_count.run(value,item)




        return self.go_next.run(value,method,condition)



class GetCount:

    def run(self,value,item):

        if type(value)==str:
            return  value.count(item)

        if type(value)==list and item in value:
            return value.count(item)

        if type(value)==list and item not in value:
            if re.sub(r'[-.+]','',str(item)).isdigit():
                return value.count(float(item))


        return 0


