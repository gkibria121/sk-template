import regex as re
class GetCondition:
    def run(self,value,condition):
        pattern = r'\(\((\w+)\)=>((?:([^()])|(\((?2)\)))*)\)'

        match = re.search(pattern,condition)

        try:
            exec(f'{match[1]} = {value}')
        except NameError:
            exec(f'{match[1]} = "{value}"')


        if eval(f'{match[2]}'):
            return True

        return False
