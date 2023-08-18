import regex as re

class SelectProcess:
    def __init__(self):
        self.go_next = None
        self.operators_process = OperatorsProcess()

    def process(self,name,argument):

        if name =='select':

            pattern =r'\:\s*(?![\"\'])((\d+(\.\d+))|([\w\.\s\+\-\/\*\^\%\(\)]+))(?![\"\'])'


            argument = re.sub(pattern , lambda match : f": {self.operators_process.run(match[4])}" if match[3] == None else  f": {match[2]}",argument)

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table
    def set_argument_process(self,argument_processor):
        self.argument_processor = argument_processor
        self.operators_process.set_argument_process(self.argument_processor)



class OperatorsProcess:

    def __init__(self):
        self.bracket = Bracket()
        self.function = Function()
        self.division = Division()
        self.multiplication = Multiplication()
        self.addition = Addition()
        self.subtraction = Subtraction()
        self.reference_process = ReferenceProcess()


        self.bracket.set_next(self.function)
        self.function.set_next(self.subtraction)
        self.subtraction.set_next(self.addition)
        self.addition.set_next(self.multiplication)
        self.multiplication.set_next(self.division)

        self.division.set_next(self.reference_process)

        self.reference_process.set_next(type('Default',(),{'process' : lambda match: match}))



    def run(self,expression):

        return self.bracket.process(expression)


    def set_argument_process(self,process):
        self.argument_process = process
        self.reference_process.set_argument_process(self.argument_process)

class Bracket:
    def process(self,expression):

        if '(' in expression:

            while True:
                expression = re.sub(r'(\(([^()]+)\))', lambda match: self.go_next.process(match[2]),expression)
                if re.search(r'(\(([^()]+)\))',expression)==None:
                    break


        return self.go_next.process( expression)

    def set_next(self,go_next):
        self.go_next = go_next
class Division:
    def process(self,expression):
        if '/' in expression:
            nodes = [eval(self.go_next.process( item)) for index, item in enumerate( expression.split('/')) if item!='']

            expression = f'{{ "$divide" : {nodes}  }}'
        return self.go_next.process( expression)
    def set_next(self,go_next):
        self.go_next = go_next

class Multiplication:
    def process(self,expression):
        if '*' in expression:
            nodes = [eval(self.go_next.process( item)) for index, item in enumerate( expression.split('*')) if item!='']

            expression = f'{{ "$multiply" : {nodes}  }}'
        return self.go_next.process( expression)
    def set_next(self,go_next):
        self.go_next = go_next

class Addition:

    def process(self,expression):

        if '+' in expression:
            nodes = [eval(self.go_next.process( item)) for index, item in enumerate( expression.split('+')) if item!='']

            expression = f'{{ "$add" : {nodes}  }}'

        return self.go_next.process( expression)

    def set_next(self,go_next):
        self.go_next = go_next

class Subtraction:
    def process(self,expression):
        if '-' in expression:
            nodes = [eval(self.go_next.process( item)) for index, item in enumerate( expression.split('-')) if item!='']

            expression = f'{{ "$subtract" : {nodes}  }}'

        return self.go_next.process( expression)

    def set_next(self,go_next):
        self.go_next = go_next



class ReferenceProcess:

    def process(self,expression):
        expression = self.argument_process.process(f':{expression}')
        expression = re.sub(r'^\s*\:','',expression)

        return self.go_next.process( expression)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_argument_process(self,process):
        self.argument_process = process

class Function:
    def process(self,expression):

        return self.go_next.process( expression)

    def set_next(self,go_next):
        self.go_next = go_next