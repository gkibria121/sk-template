import regex as re
import math




class Slice:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):

        if method == 'slice':

            if len(condition) == 1 :
                condition = condition+':'
            if condition == '-1':
                condition = '::-1'
            if len(condition)>1:
                condition = condition.replace(',',':')

            value = eval(f"{value}[{condition}]")


        return self.go_next.run(value,method,condition)