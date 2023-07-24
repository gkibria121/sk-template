import regex as re
import math



class Ceil:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='ceil':

            if condition =='':
                value =math.ceil(value)
            else:
                precision = float(condition)
                value = float(value)
                mod = value % precision

                if mod == 0:
                    value = str(value)
                else:
                    value = str(value + precision - mod)

        return self.go_next.run(value,method,condition)

