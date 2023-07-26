import regex as re
import math



class Capitalize:
    def set_next(self,go_next):
        self.go_next = go_next
    def __init__(self):
        self.convert_to_capitalize= ConvertToCapitalize()

    def run(self,value,method,condition):


        if method =='capitalize':

            if condition =='':
                value = self.convert_to_capitalize.run(value)
            if condition !='':
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    exec(f"{match[1]} = value")
                    if eval(f"{match[2]}"):
                        value = self.convert_to_capitalize.run(value)

        return self.go_next.run(value,method,condition)


class ConvertToCapitalize:
    def run(self,value):
        pattern = r'(\s*)(\b|\W|_)(\w)(\w+)?'
        value =re.sub(pattern,lambda match : match[1]+match[2]+match[3].upper()+match[4].lower() if match[4]!=None else match[1]+match[2]+match[3].upper()  , value)
        return value
