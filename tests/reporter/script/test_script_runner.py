import io
import sys

class ScriptRunner:

    def __init__(self):
        self.successor = None
        self.go_next = None

    def run(self, scripts):
        template_script, row_script = scripts

        code_string = row_script
        output_stream = io.StringIO()
        sys.stdout = output_stream
        exec(code_string)
        sys.stdout = sys.__stdout__
        captured_output = output_stream.getvalue()

        return template_script, captured_output

    def set_succesor(self, successor):
        self.successor = successor

    def set_next(self, go_next):
        self.go_next = go_next
