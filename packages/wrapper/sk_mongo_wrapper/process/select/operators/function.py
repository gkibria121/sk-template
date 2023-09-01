import regex as re

class Function:
    def process(self,expression):

        pattern = r'\b([a-zA-Z_]+\w+)\s*\(([^()]+)\)'

        while re.search(pattern,expression):
            expression = re.sub(pattern,lambda match : f'{{ "${match[1]}" : {self.go_next.process(match[2])} }}',expression)


        return self.go_next.process( expression)

    def set_next(self,go_next):
        self.go_next = go_next