import regex as re
import math



class Ceil:
    def set_next(self,go_next):
        self.go_next = go_next

    def __init__(self):
        self.get_ceil = GetCeil()
        self.get_significance = GetSignigicance()

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

class GetSignigicance:
    def run(self,condition):
        condition = re.sub(r'\((\w+)\)=>((?:([^(),])|(\((?2)\)))*)','',condition)
        if re.sub(r'[+-.]','',condition).isdigit():
            num = condition.replace(',','')
            return num



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