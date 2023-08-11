class WhereProcess:
    def __init__(self):
        self.go_next = None
        self.process_operators = ProcessOperators()

    def process(self,name,argument):
        if name == 'where':

            argument = self.process_operators.run(argument)

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table


class ProcessOperators:

    def __init__(self):
        self.gt = GreaterThen()

    def run(self,argument):

        return argument


class GreaterThen:

    def process(self,argument):

        return argument




