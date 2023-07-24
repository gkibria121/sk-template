import regex as re
import math



class Min:

    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='min':

            if condition =='':
                value =min(value)
            else:
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:

                    value = eval(f"min([{match[1]} for {match[1]} in value if {match[2]} ])")



        return self.go_next.run(value,method,condition)