import regex as re
import math



class CamelCase:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='camel':

            if condition =='':
                pattern = r'\s*\b(\w)'
                value =re.sub(pattern,lambda match : match[1].upper() , value)

        return self.go_next.run(value,method,condition)