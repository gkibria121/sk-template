import regex as re
import math

from .modules.get_arg import GetArg
class Count:
    def __init__(self):
        self.get_item = GetArg()
        self.get_count = GetCount()

    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='count':

            if condition =='':
                value =0
            if condition !='':
                pattern = r'\((\w+)\)=>((?:([^(),])|(\((?2)\)))*)'
                match = re.search(pattern,condition)
                if match:
                    exec(f"{match[1]} = value")
                    if eval(f"{match[2]}"):
                        item = self.get_item.run(condition)
                        value = self.get_count.run(value,item)
                    else:
                        value = str(value)
                else:
                    item = self.get_item.run(condition)
                    value = self.get_count.run(value,item)



        return self.go_next.run(value,method,condition)



class GetCount:

    def run(self,value,item):

        if type(value)==str:
            return  str(value.count(item))

        if type(value)==list and item in value:
            return str(value.count(item))

        if type(value)==list and item not in value:
            if re.sub(r'[-.+]','',str(item)).isdigit():
                return str(value.count(float(item)))


        return '0'


