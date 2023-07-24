import regex as re
import math



class SnakeCase:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='snake':

            if condition =='':
                pattern = r'\s+'
                value =re.sub(pattern,'_' , value.lower())

        return self.go_next.run(value,method,condition)