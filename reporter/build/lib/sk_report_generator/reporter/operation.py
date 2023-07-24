import regex as re

class OperationHandler:

    def __init__(self):
        self.successor = None
        self.eval = EvaluateOperation()
    def report(self,template):
        pattern = r'\{(\{((?:[^{}]|(?1))*)\})\}'
        matches = re.findall(pattern,template)
        for match in matches:
            result = self.eval.run(match)
            template = re.sub(re.escape(match[0]),result,template)
        return self.successor.report(template)


    def set_successor(self, successor):
        self.successor = successor

    def set_data(self, data):
        self.data = data


class EvaluateOperation:

    def run(self,operation):
        eval_pattern = r'eval(\((?>[^()]|(?1))*\))'
        matches = re.findall(eval_pattern, operation[0])
        result = operation[0]
        for match in matches:
            value = eval(match)
            result = re.sub(r'eval\s*' + re.escape(match), str(value), result)
        return result

