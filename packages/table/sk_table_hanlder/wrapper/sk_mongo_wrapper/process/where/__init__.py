import regex as re


class WhereProcess:
    def __init__(self):
        self.go_next = None
        self.process_operators = ProcessOperators()
        self.index_process = IndexProcess()
        self.process_operators.set_index_process(self.index_process)


    def process(self,name,argument):
        if name == 'where':

            argument = self.process_operators.run(argument)

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table
        self.index_process.set_primary_table(self.primary_table)


class IndexProcess:

    def run(self,index):

        pattern = r'((?<!\.)(\b)(' +re.escape(self.primary_table) +r')\.)'

        return re.sub(pattern,lambda match : f"$",index)

    def set_primary_table(self,table):
        self.primary_table = table






class ProcessOperators:

    def __init__(self):
        self.gt = GreaterThen()
        self.lt = LessThen()
        self.gte = GreaterThenEqual()
        self.lte = LessThenEqual()
        self.eq = EqualTo()
        self.ne = NotEqual()

        self.gt.set_next(self.lt)
        self.lt.set_next(self.gte)
        self.gte.set_next(self.lte)
        self.lte.set_next(self.eq)
        self.eq.set_next(self.ne)
        self.ne.set_next(type('Default' ,(),{'process' : lambda argument: argument}  ) )


    def set_index_process(self,process):
        self.process = process
        self.gt.set_index_process(self.process)
        self.lt.set_index_process(self.process)
        self.gte.set_index_process(self.process)
        self.lte.set_index_process(self.process)
        self.eq.set_index_process(self.process)
        self.ne.set_index_process(self.process)

    def run(self,argument):




        return  self.gt.process(argument)


class GreaterThen:


    def process(self,argument):

        if re.search(r'(?=\b)\s*>\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*>\s*(?=[^=])',argument)) if item!='']
            key = self.index_process.run(result[0])
            value = result[1]
            argument = f'{{ "{key}" : {{ "$gt" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_index_process(self,process):
        self.index_process = process

class LessThen:

    def process(self,argument):

        if re.search(r'(?=\b)\s*<\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*<\s*(?=[^=])',argument)) if item!='']
            key = self.index_process.run(result[0])
            value = result[1]
            argument = f'{{ "{key}" : {{ "$lt" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_index_process(self,process):
        self.index_process = process

class EqualTo:

    def process(self,argument):

        if re.search(r'(?=\b)\s*==\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*==\s*(?=[^=])',argument)) if item!='']
            key = self.index_process.run(result[0])
            value = result[1]
            argument = f'{{ "{key}" : {{ "$eq" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_index_process(self,process):
        self.index_process = process

class NotEqual:

    def process(self,argument):

        if re.search(r'(?=\b)\s*==\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*==\s*(?=[^=])',argument)) if item!='']
            key = self.index_process.run(result[0])
            value = result[1]
            argument = f'{{ "{key}" : {{ "$ne" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_index_process(self,process):
        self.index_process = process


class GreaterThenEqual:

    def process(self,argument):

        if re.search(r'(?=\b)\s*>=\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*>=\s*(?=[^=])',argument)) if item!='']
            key = self.index_process.run(result[0])
            value = result[1]
            argument = f'{{ "{key}" : {{ "$gte" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_index_process(self,process):
        self.index_process = process

class LessThenEqual:

    def process(self,argument):

        if re.search(r'(?=\b)\s*<=\s*(?=[^=])',argument):
            result = [item for index,item in enumerate(  re.split(r'(?=\b)\s*<=\s*(?=[^=])',argument)) if item!='']
            key = self.index_process.run(result[0])
            value = result[1]
            argument = f'{{ "{key}" : {{ "$lte" : {value}   }} }}'

        return self.go_next.process(argument)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_index_process(self,process):
        self.index_process = process