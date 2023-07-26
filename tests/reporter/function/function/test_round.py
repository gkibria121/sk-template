import regex as re
import math



class Round:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='round':

            if condition !='':
                value =round(value,int(condition))

        return self.go_next.run(value,method,condition)