import regex as re
class GetIndexValue:

    def __init__(self):
        self.data = None

    def run(self,value,index):
        if type(value) == list:
            value = value
            index_list = re.split(r'(?<=[\]])(?=[\[])',index)

            for index in index_list:
                if re.sub('[\[\]\"]','',index).isdigit() or type(value)==dict:
                    value = eval(f"{value}{index}")
                else :
                    value = eval(f'[item{index} for index,item in enumerate(value)]')


            return value


        if type(value) == dict:
            indexd = re.sub(r'[\[\]]','',index)
            if indexd.isdigit():
                value = list(value.keys())

            return eval(f"{value}{index}")


    def set_data(self,data):
        self.data = data