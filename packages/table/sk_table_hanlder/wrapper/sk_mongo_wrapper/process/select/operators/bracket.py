import regex as re
class Bracket:
    def process(self,expression):

        if '(' in expression:

            while True:
                expression = re.sub(r'(?<!\w)(\(([^()]+)\))', lambda match: self.go_next.process(match[2]),expression)
                if re.search(r'(?<!\w)(\(([^()]+)\))',expression)==None:
                    break


        return self.go_next.process( expression)

    def set_next(self,go_next):
        self.go_next = go_next