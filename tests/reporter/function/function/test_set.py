import regex as re
import math



class Set:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='set':

            if condition =='':
                value =set(value)

        return self.go_next.run(value,method,condition)