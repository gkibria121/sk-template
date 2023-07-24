import regex as re
import math


class Avg:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='avg':

            if condition =='':
                value =sum(value)/len(value)
            else:

                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    value= eval(f"sum([{match[1]} for {match[1]} in value if {match[2]} ])/len([{match[1]} for {match[1]} in value if {match[2]} ])")


        return self.go_next.run(value,method,condition)