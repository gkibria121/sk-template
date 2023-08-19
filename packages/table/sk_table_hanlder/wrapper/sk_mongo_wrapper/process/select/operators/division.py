import regex as re



class Division:
    def process(self,expression):
        if '/' in expression:
            nodes = [eval(self.go_next.process( item)) for index, item in enumerate( expression.split('/')) if item!='']

            expression = f'{{ "$divide" : {nodes}  }}'
        return self.go_next.process( expression)
    def set_next(self,go_next):
        self.go_next = go_next

