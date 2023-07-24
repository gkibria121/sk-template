import regex as re


class ScriptProcess:

    def __init__(self):
        self.successor = None
        self.go_next = None
        self.script_print_process = ScriptPrintProcess()

    def run(self, script):
        template_script, row_script = script
        value = self.successor.report(row_script)
        pattern = r'(<<(.*?)>>)'
        matches = re.findall(pattern, value)
        for match in matches:
            code = self.script_print_process.process_code(match[1])
            printf = "print(f'" + code + "')"
            value = re.sub(re.escape(match[0]), printf, value)

        return self.go_next.run((template_script, value))

    def set_succesor(self, successor):
        self.successor = successor

    def set_next(self, go_next):
        self.go_next = go_next


class ScriptPrintProcess:

    def __init__(self):
        pass

    def process_code(self, code):
        format_pattern = '{[^{}]+}'
        matches = re.findall(format_pattern, code)
        for match in matches:
            pattern = r'(?:(?<!:)(?:\.([^\W\d][\w]*))\b(?!\())'
            format_value = re.sub(pattern, lambda match: f'["{match.group(1)}"]', match)
            code = re.sub(re.escape(match), format_value, code)
        return code
