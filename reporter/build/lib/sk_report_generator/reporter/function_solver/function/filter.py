import regex as re
import math


class Filter:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):

        if method == 'filter':

            pattern = r'\s*\(([\w\,]+)\)\s*=>\s*(.*)'
            match = re.search(pattern,condition)
            if match:
                event =match[1]
                condition = match[2]
                if type(value) == list:

                    temp = []
                    for item in value:
                        exec(f"{event} = {item}")
                        filt = eval(f"{condition}")
                        if filt:
                            temp.append(item)


                    value = temp

                if type(value) == set:

                    temp = set()
                    for item in value:
                        exec(f"{event} = {item}")
                        filt = eval(f"{condition}")
                        if filt:
                            temp.add(item)
                    value = temp


            value = eval(f"{value}[{condition}]")


        return self.go_next.run(value,method,condition)