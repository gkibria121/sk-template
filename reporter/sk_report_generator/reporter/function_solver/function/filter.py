import regex as re
import math


class Filter:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):

        if method == 'filter':
            if condition=='':
                pass
            if condition!='':
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    if type(value) == list:
                        value = eval(f"[{match[1]} for {match[1]} in value if {match[2]}]")

                    if type(value) == set:
                        value = eval(f"{{{match[1]} for {match[1]} in value if {match[2]}}}")



        return self.go_next.run(value,method,condition)