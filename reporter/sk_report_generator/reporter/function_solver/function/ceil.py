import regex as re
import math
from .modules.get_arg import GetArg


class Ceil:
    def set_next(self,go_next):
        self.go_next = go_next

    def __init__(self):
        self.get_ceil = GetCeil()
        self.get_significance = GetArg()

    def run(self,value,method,condition):


        if method =='ceil':

            if condition =='':
                value =str(math.ceil(value)/1.0)
            if condition !='':
                pattern = r'\((\w+)\)=>((?:([^(),])|(\((?2)\)))*)'
                match = re.search(pattern,condition)
                if match:
                    exec(f"{match[1]} = value")
                    if eval(f"{match[2]}"):
                        significance = self.get_significance.run(condition)
                        value = self.get_ceil.run(value,significance)
                    else:
                        value = str(value)
                else:
                    value = self.get_ceil.run(value,condition)

        return self.go_next.run(value,method,condition)





class GetCeil:

    def run(self,value,significance):
        precision = float(significance)
        value = float(value)
        mod = value % precision

        if mod == 0:
            value = str(float(value))
        else:
            value = str(float(value + precision - mod))
        return value