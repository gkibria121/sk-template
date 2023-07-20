import regex as re

class Foreach:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='foreach':

            if condition !='':
                pattern = r'\(([\w,]+)\)\=\>(\{(([^{}]|(?2))*)\})'
                match = re.search(pattern,condition)
                obj = value if type(value) == list else value.items()
                script =f'''
for {match[1]} in {obj}:
    pass
'''


        return self.go_next.run(value,method,condition)