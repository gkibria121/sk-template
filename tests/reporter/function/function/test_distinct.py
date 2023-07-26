import regex as re
import math

class Distinct:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='distinct':

            if condition =='':
                value =list(set(value))

        return self.go_next.run(value,method,condition)