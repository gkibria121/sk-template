import regex as re
import math



class Reverse:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='reverse':

            if condition =='':
                value =value.reverse()

        return self.go_next.run(value,method,condition)