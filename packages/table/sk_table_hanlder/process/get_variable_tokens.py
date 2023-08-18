import regex as re


class GetVariableTokens:
    def run(self,declarations):

        pattern = r'(?:(\$\w+)\s*=\s*([^;]+));'
        tokens = re.findall(pattern,declarations)

        return tokens
