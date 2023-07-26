import regex as re
import math



class SnakeCase:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='snake':

            if condition =='':
                # convert Camel Case to Snake Case
                value = re.sub(r'(?<=[a-z])(?=[A-Z])','_',value)

                # convert  to Snake Case
                value =re.sub( r'(?<=\b)(\s+)(?=\w)','_' , value.lower())

                # remove extra space
                value =re.sub(r'\s*','' , value)

        return self.go_next.run(value,method,condition)

