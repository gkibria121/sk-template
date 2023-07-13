import regex as re
import math



class Capitalize:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='capitalize':

            if condition =='':
                value =value.capitalize()

        return self.go_next.run(value,method,condition)