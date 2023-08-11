import io
import sys

class ScriptRunner:

    def __init__(self):
        self.successor = None
        self.go_next = None
        self.evaluate_script = EvaluateScript()


    def run(self, scripts):
        template_script, row_script = scripts



        result = self.evaluate_script.run(row_script)

        return template_script, result

    def set_succesor(self, successor):
        self.successor = successor

    def set_next(self, go_next):
        self.go_next = go_next

class EvaluateScript:

    def run(self,script):
        code_string = script
        output_stream = io.StringIO()
        sys.stdout = output_stream
        exec(code_string)
        sys.stdout = sys.__stdout__
        captured_output = output_stream.getvalue()

        return captured_output

