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

class Max:

    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='max':

            if condition =='':
                value =max(value)
            else:
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:

                    value = eval(f"max([{match[1]} for {match[1]} in value if {match[2]} ])")



        return self.go_next.run(value,method,condition)

class Len:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='len':

            if condition =='':
                value =len(value)
            else:

                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    value= eval(f"len([{match[1]} for {match[1]} in value if {match[2]} ])")


        return self.go_next.run(value,method,condition)

class Avg:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='avg':

            if condition =='':
                value =sum(value)/len(value)
            else:

                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    value= eval(f"sum([{match[1]} for {match[1]} in value if {match[2]} ])/len([{match[1]} for {match[1]} in value if {match[2]} ])")


        return self.go_next.run(value,method,condition)
class Len:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='len':

            if condition =='':
                value =len(value)
            else:
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    value= eval(f"len([{match[1]} for {match[1]} in value if {match[2]} ])")





        return self.go_next.run(value,method,condition)

class Count:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='count':

            if condition !='':
                value =value.count(float(condition))



        return self.go_next.run(value,method,condition)


class Reverse:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='reverse':

            if condition =='':
                value =value.reverse()

        return self.go_next.run(value,method,condition)
class Set:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='set':

            if condition =='':
                value =set(value)

        return self.go_next.run(value,method,condition)

class Distinct:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='distinct':

            if condition =='':
                value =list(set(value))

        return self.go_next.run(value,method,condition)

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



class Slice:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):

        if method == 'slice':

            if len(condition) == 1 :
                condition = condition+':'
            if condition == '-1':
                condition = '::-1'
            if len(condition)>1:
                condition = condition.replace(',',':')

            value = eval(f"{value}[{condition}]")


        return self.go_next.run(value,method,condition)



class Ceil:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='ceil':

            if condition =='':
                value =math.ceil(value)

        return self.go_next.run(value,method,condition)



class Round:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='round':

            if condition !='':
                value =round(value,int(condition))

        return self.go_next.run(value,method,condition)




class Floor:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='floor':

            if condition =='':
                value =math.floor(value)

        return self.go_next.run(value,method,condition)

class Sum:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):

        if method =='sum':

            if condition =='':
                value =sum(value)
            else:
                pattern = r'\s*\((\w+)\)\s*=>\s*(.*)'
                match = re.search(pattern,condition)
                if match:
                    value= eval(f"sum([{match[1]} for {match[1]} in value if {match[2]} ])")

        return self.go_next.run(value,method,condition)

class MethodDefault:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):
        return value
