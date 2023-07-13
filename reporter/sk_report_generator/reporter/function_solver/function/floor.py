import regex as re
import math





class Floor:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='floor':

            if condition =='':
                value =math.floor(value)

        return self.go_next.run(value,method,condition)