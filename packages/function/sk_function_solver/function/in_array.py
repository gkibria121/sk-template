import regex as re
import math


class In:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):

        if method in ['in']:
            if condition=='':
                pass
            if condition!='':
                if type(value) == list:
                    condition = eval(f"next((x for x in value if x=={condition}), False)")

                    if condition:
                        value = True
                    else:
                        value = False






        return self.go_next.run(value,method,condition)