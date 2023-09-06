import regex as re
class ProcessFunctionCalling:
    def __init__(self):
        pass
    def run(self,function_calling):

        pattern = r'(?:(?<!:)\s*(?:\.([^\d][\w]*))\b(?!\())'
        function_calling = re.sub(pattern, lambda match: f'["{match.group(1)}"]', function_calling)

        return function_calling