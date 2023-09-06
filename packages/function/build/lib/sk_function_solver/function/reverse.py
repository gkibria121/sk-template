from .modules.check_condition import CheckCondition
import regex as re
import math



class Reverse:
    def __init__(self):
        self.check_condition =CheckCondition()

    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='reverse':

            if condition =='':
                if type(value) ==str:
                    value = value[::-1]
                else:
                    value.reverse()
            if condition!='':
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    if type(value) == list:
                        value = eval(f"[{match[1]} for {match[1]} in value if {match[2]}]")
                        value.reverse()
                    if type(value) == set:
                        value = eval(f"{{{match[1]} for {match[1]} in value if {match[2]}}}")
                        value.reverse()
                    if type(value)==str:
                        value = value[::-1]



        return self.go_next.run(value,method,condition)