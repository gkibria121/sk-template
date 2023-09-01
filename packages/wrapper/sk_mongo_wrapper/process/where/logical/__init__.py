import regex as re
class LogicalOperatorsProcess:


    def __init__(self):
        self.and_process = And()
        self.or_process = Or()
        self.in_process = In()
        self.nin_process = NotIn()
        self.and_process.set_next(self.nin_process)
        self.nin_process.set_next(self.in_process)
        self.in_process.set_next(self.or_process)
        self.or_process.set_next(type('Default' ,(),{'process' : lambda argument: argument}  ) )

    def process(self,argument):

        argument =self.and_process.process(argument)

        argument = self.process_operators.run(argument)

        return argument


    def set_process_operators(self,process):
        self.process_operators = process
        self.and_process.set_process_operators(self.process_operators)
        self.or_process.set_process_operators(self.process_operators)
        self.in_process.set_process_operators(self.process_operators)

class And:
    def process(self,argument):
        pattern =r'((\W?(([\w\.]+)|(\d+(\.\d+)*))\W?([\W]+)\W?(([\w\.]+)|(\d+(\.\d+)*)))\W?|((\{([^{}]|(?13))*\})))\s*AND\s*((?1))'

        if re.search(pattern,argument):
            argument = re.sub(pattern,lambda match: f'{{ "$and" : [{self.process_operators.run(match[1])},{self.process_operators.run(match[15])}]   }}',argument)
        return self.go_next.process(argument)

    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next

class Or:
    def process(self,argument):

        pattern =r'((\W?(([\w\.]+)|(\d+(\.\d+)*))\W?([\W]+)\W?(([\w\.]+)|(\d+(\.\d+)*)))\W?|((\{([^{}]|(?13))*\})))\s*OR\s*((?1))'

        if re.search(pattern,argument):
            argument = re.sub(pattern,lambda match: f'{{ "$or" : [{self.process_operators.run(match[1])},{self.process_operators.run(match[15])}]   }}',argument)

        return self.go_next.process(argument)


    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next



class In:
    def process(self,argument):


        pattern =r'((\W?(([\w\.]+)|(\d+(\.\d+)*))\W?([\W]+)\W?(([\w\.]+)|(\d+(\.\d+)*)))\W?|((\{([^{}]|(?13))*\})))\s*IN\s*(\[([^\[\]]|(?15))*\])'

        if re.search(pattern,argument):
            argument = re.sub(pattern,lambda match: f'{{ "{self.process_operators.run(match[1])}" : {{ "$in" : {self.process_operators.run(match[15])} }}  }}',argument)


        return self.go_next.process(argument)

    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next
class Not:
    def process(self,argument):

        pattern =r'\s*NOT\s*((\W?(([\w\.]+)|(\d+(\.\d+)*))\W?([\W]+)\W?(([\w\.]+)|(\d+(\.\d+)*)))\W?|((\{([^{}]|(?13))*\})))'

        if re.search(pattern,argument):
            argument = re.sub(pattern,lambda match: f'{{ "$not" : {self.process_operators.run(match[1])} }}',argument)

        return self.go_next.process(argument)


    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next

class NotIn:
    def process(self,argument):

        pattern =r'((\W?(([\w\.]+)|(\d+(\.\d+)*))\W?([\W]+)\W?(([\w\.]+)|(\d+(\.\d+)*)))\W?|((\{([^{}]|(?13))*\})))\s*NOT IN\s*(\[([^\[\]]|(?15))*\])'

        if re.search(pattern,argument):
            argument = re.sub(pattern,lambda match: f'{{ "{self.process_operators.run(match[1])}" : {{ "$nin" : {self.process_operators.run(match[15])} }}  }}',argument)


        return self.go_next.process(argument)
    def set_process_operators(self,process):
        self.process_operators = process


    def set_next(self,go_next):
        self.go_next = go_next