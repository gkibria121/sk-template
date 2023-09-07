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

                pattern = r'(\(((\(\w+\))|(\w+))\s*=>\s*(([^()]|(\((?5)\)))*)\)\s*\,)?(([^|]+)(\|(.*))?)'
                match = re.search(pattern,condition)
                if match:

                    if type(value)==list:
                        print(value)

                        placeholder = match[3] if match[3] is not None else match[4]
                        eb = placeholder if match[11] is None else match[11]


                        value= eval(f"[{match[9]}  if {match[5]}  else {eb} for {placeholder} in value]")


        return self.go_next.run(value,method,condition)