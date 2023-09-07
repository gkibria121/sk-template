import regex as re
import math


class Select:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='select':

            if condition =='':
                value = value
            else:

                pattern = r'(\(((\(\w+\))|(\w+))\s*=>\s*(([^()]|(\((?5)\)))*)\)\s*\,)?(.*)'
                match = re.search(pattern,condition)
                if match:

                    if type(value)==list:
                        print(value)

                        placeholder = match[3] if match[3] is not None else match[4]


                        value= eval(f"[{match[8]}  if {match[5]}  else {placeholder} for {placeholder} in value]")


        return self.go_next.run(value,method,condition)