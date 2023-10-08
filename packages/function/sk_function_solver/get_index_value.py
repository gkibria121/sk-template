import regex as re
class GetIndexValue:

    def __init__(self):
        self.data = None

    def run(self,value,index):
        if type(value)==list:
            if re.search(r'\[\d+\]',index):
                return eval(f'{value}{index}')
            r_value = []
            for item in value:
                if type(item) == list:
                    r_value += eval(f'[item2{index} for index,item2 in enumerate(item)]')
            if len(r_value)==0:

                return eval(f'[item{index} for index,item in enumerate(value)]')
            return r_value


        if type(value) == dict:
            indexd = re.sub(r'[\[\]]','',index)
            if indexd.isdigit():
                value = list(value.keys())

            return eval(f"{value}{index}")


    def set_data(self,data):
        self.data = data