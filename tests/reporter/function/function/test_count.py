import regex as re
import math


class Count:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='count':

            if condition !='':
                value =value.count(float(condition))



        return self.go_next.run(value,method,condition)