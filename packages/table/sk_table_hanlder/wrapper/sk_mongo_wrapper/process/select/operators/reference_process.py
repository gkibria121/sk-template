import regex as re

class ReferenceProcess:

    def process(self,expression):
        expression = self.argument_process.process(f':{expression}')
        expression = re.sub(r'^\s*\:','',expression)

        return self.go_next.process( expression)

    def set_next(self,go_next):
        self.go_next = go_next

    def set_argument_process(self,process):
        self.argument_process = process