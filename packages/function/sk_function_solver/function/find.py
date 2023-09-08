import regex as re
import math


class Find:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):

        if method in ['find','find_first']:
            if condition=='':
                pass
            if condition!='':
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    if type(value) == list:
                        value = eval(f"next(({match[1]} for {match[1]} in value if {match[2]}), -1)")

        if method in ['find_last']:
            if condition=='':
                pass
            if condition!='':
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    if type(value) == list:
                        value = eval(f"next(({match[1]} for {match[1]} in value[::-1] if {match[2]}), -1)")




        return self.go_next.run(value,method,condition)