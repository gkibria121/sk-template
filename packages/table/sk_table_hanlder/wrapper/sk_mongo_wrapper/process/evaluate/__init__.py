import io
import sys

class EvaluateScript:

    def run(self,script):
        code_string = script
        output_stream = io.StringIO()
        sys.stdout = output_stream
        exec(code_string)
        sys.stdout = sys.__stdout__
        captured_output = output_stream.getvalue().strip()

        return captured_output