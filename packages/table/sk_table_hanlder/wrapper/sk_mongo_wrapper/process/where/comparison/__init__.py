import regex as re


class ProcessOperators:

    def __init__(self):
        self.gt = GreaterThen()
        self.lt = LessThen()
        self.gte = GreaterThenEqual()
        self.lte = LessThenEqual()
        self.eq = EqualTo()
        self.equalt = Equal()
        self.ne = NotEqual()

        self.gt.set_next(self.lt)
        self.lt.set_next(self.gte)
        self.gte.set_next(self.lte)
        self.lte.set_next(self.equalt)
        self.equalt.set_next(self.eq)
        self.eq.set_next(self.ne)
        self.ne.set_next(type('Default' ,(),{'process' : lambda argument: argument}  ) )


    def run(self,argument):




        return  self.gt.process(argument)


class GreaterThen:


    def process(self,argument):

        if re.search(r'(?=\b)\s*>\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*>\s*(?=[^=])',argument)) if item!='']
            key = result[0].replace(' ','')
            value = result[1]
            argument = f'{{ "{key}" : {{ "$gt" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next


class LessThen:

    def process(self,argument):

        if re.search(r'(?=\b)\s*<\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*<\s*(?=[^=])',argument)) if item!='']
            key = result[0].replace(' ','')
            value = result[1]
            argument = f'{{ "{key}" : {{ "$lt" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next


class EqualTo:

    def process(self,argument):

        if re.search(r'(?=\b)\s*==\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*==\s*(?=[^=])',argument)) if item!='']
            key = result[0].replace(' ','')
            value = result[1]
            argument = f'{{ "{key}" : {{ "$eq" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next



class NotEqual:

    def process(self,argument):

        if re.search(r'(?=\b)\s*!=\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*!=\s*(?=[^=])',argument)) if item!='']
            key = result[0].replace(' ','')
            value = result[1]
            argument = f'{{ "{key}" : {{ "$ne" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next



class GreaterThenEqual:

    def process(self,argument):

        if re.search(r'(?=\b)\s*>=\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*>=\s*(?=[^=])',argument)) if item!='']
            key = result[0].replace(' ','')
            value = result[1]
            argument = f'{{ "{key}" : {{ "$gte" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next


class LessThenEqual:

    def process(self,argument):

        if re.search(r'(?=\b)\s*<=\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*<=\s*(?=[^=])',argument)) if item!='']
            key = result[0].replace(' ','')
            value = result[1]
            argument = f'{{ "{key}" : {{ "$lte" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next

class Equal:

    def process(self,argument):

        if re.search(r'(?=\b)\s*=\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*=\s*(?=[^=])',argument)) if item!='']
            key = result[0].replace(' ','')
            value = result[1]
            argument = f'{{ "{key}" : {{ "$eq" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next