from .modules.check_condition import CheckCondition
import regex as re
import math



class Set:
    def __init__(self):
        self.check_condition =CheckCondition()

    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='set':

            if condition =='':
                value = set(value)
            if condition!='':
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    value = eval(f"{{{match[1]} for {match[1]} in value if {match[2]}}}")





        return self.go_next.run(value,method,condition)