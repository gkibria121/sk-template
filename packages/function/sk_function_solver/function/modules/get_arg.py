import regex as re
class GetArg:
    def run(self,condition):
        if condition=='':
            return '1'
        condition = re.sub(r'\((\w+)\)=>((?:([^(),])|(\((?2)\)))*)(,)?','',condition)
        if re.sub(r'[+-.]','',condition).isdigit():
            num_list = [item for index,item in enumerate(re.split(',',condition)) if item != '']
            for num in num_list:
                if re.sub(r'[-.+]','',num).isdigit():
                    return num


        return re.sub(r'^\s*','',condition)

