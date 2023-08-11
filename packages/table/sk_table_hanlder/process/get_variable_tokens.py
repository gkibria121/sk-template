import regex as re


class GetVariableTokens:
    def run(self,declarations):
        pattern = r'(\$\w+\s*=\s*[^;]+);'
        tokens = [self.get_key_value(item) for index,item in enumerate( re.split(pattern,declarations)) if item !='' and item !='\n']
        tokens = [item for index,item in enumerate(tokens) if item !=None ]

        return tokens

    def get_key_value(self,item):
        pattern = r'(\$\w+)\s*=([^;]+)'
        if len(re.findall(pattern,item))>0:
            return re.findall(pattern,item)[0]
