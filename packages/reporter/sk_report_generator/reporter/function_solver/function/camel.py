from .modules.check_condition import CheckCondition
import regex as re
import math



class CamelCase:
    def set_next(self,go_next):
        self.go_next = go_next
    def __init__(self):
        self.convert_to_camel= ConvertToCamel()
        self.check_condition = CheckCondition()

    def run(self,value,method,condition):


        if method =='camel':

            if condition =='':
                value = self.convert_to_camel.run(value)
            if condition !='':
                if self.check_condition.run(value,condition):
                    value = self.convert_to_camel.run(value)
        return self.go_next.run(value,method,condition)


class ConvertToCamel:
    def run(self,value):
        pattern = r'\s*(\b|\W|_)(\w)(\w+)?'
        value =re.sub(pattern,lambda match : match[2].upper()+match[3].lower() if match[3]!=None else match[2].upper()  , value)
        if '_' in value:
            value =re.sub(r'_(\w)(\w*?)(?=[A-Z 0-9_])',lambda match : match[1].upper()+match[2].lower() , value)
        return value
