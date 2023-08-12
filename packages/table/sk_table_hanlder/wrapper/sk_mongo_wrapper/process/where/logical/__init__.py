import regex as re
class LogicalOperatorsProcess:


    def __init__(self):
        self.and_process = And()
        self.or_process = Or()
        self.in_process = In()
        self.nin_process = NotIn()
        self.and_process.set_next(self.in_process)
        self.in_process.set_next(self.nin_process)
        self.nin_process.set_next(self.or_process)
        self.or_process.set_next(type('Default' ,(),{'process' : lambda argument: argument}  ) )

    def process(self,argument):

        return self.and_process.process(argument)


    def set_process_operators(self,process):
        self.process_operators = process
        self.and_process.set_process_operators(self.process_operators)
        self.or_process.set_process_operators(self.process_operators)
        self.in_process.set_process_operators(self.process_operators)

class And:
    def process(self,argument):

        if re.search(r'\s*\$and\s*',argument):
            result = [eval(self.process_operators.run(item)) for index,item in enumerate(  re.split(r'\s*\$and\s*',argument)) if item!='']
            argument = f'{{ "$and" : {result} }}'

        return self.go_next.process(argument)

    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next

class Or:
    def process(self,argument):

        if re.search(r'\s*\$or\s*',argument):
            result = [self.process_operators.run(item) for index,item in enumerate(  re.split(r'\s*\$or\s*',argument)) if item!='']
            argument = f'{{ "$or" : {result} }}'

        return self.go_next.process(argument)

    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next



class In:
    def process(self,argument):

        if re.search(r'\s*\$in\s*',argument):
            result = [self.process_operators.run(item) for index,item in enumerate(  re.split(r'\s*\$in\s*',argument)) if item!='']

            key =result[0].replace(" ","")

            value = result[1]


            argument = f'{{ "{key}" : {{ "$in" : {value} }} }}'

        return self.go_next.process(argument)

    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next

class NotIn:
    def process(self,argument):

        if re.search(r'\s*\$nin\s*',argument):
            result = [self.process_operators.run(item) for index,item in enumerate(  re.split(r'\s*\$nin\s*',argument)) if item!='']

            key =result[0].replace(" ","")

            value = result[1]


            argument = f'{{ "{key}" : {{ "$nin" : {value} }} }}'

        return self.go_next.process(argument)

    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next