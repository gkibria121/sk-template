import regex as re
import math



class LowerCase:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='lower':

            if condition =='':
                value =value.lower()

        return self.go_next.run(value,method,condition)