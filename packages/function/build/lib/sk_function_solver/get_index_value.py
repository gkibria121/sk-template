import regex as re
class GetIndexValue:

    def __init__(self):
        self.data = None

    def run(self,value,index):
        if type(value)==list:
            if re.search(r'\[\d+\]',index):
                return eval(f'{value}{index}')
            return eval(f'[item{index} for index,item in enumerate(value)]')


        if type(value) == dict:
            indexd = re.sub(r'[\[\]]','',index)
            if indexd.isdigit():
                value = list(value.keys())

            return eval(f"{value}{index}")


    def set_data(self,data):
        self.data = data