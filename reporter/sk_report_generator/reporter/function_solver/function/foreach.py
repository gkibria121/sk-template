import regex as re
import io
import sys

class Foreach:
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):


        if method =='foreach':

            if condition !='':
                pattern = r'\(([\w,$]+)\)\=\>(\{(([^{}]|(?2))*)\})'
                match = re.search(pattern,condition)
                obj = value
                script = f"for {match[1]} in {value}:\n"+match[3]

                code_string = script
                output_stream = io.StringIO()
                sys.stdout = output_stream
                exec(script)
                sys.stdout = sys.__stdout__
                captured_output = output_stream.getvalue()

                value = captured_output

        return self.go_next.run(value,method,condition)