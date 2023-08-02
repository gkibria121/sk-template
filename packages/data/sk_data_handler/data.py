
import regex as re

class DataStructure:
    def __init__(self):
        self.random = None
        self.variable = None
        self.table = None


    def run(self,data_text):

        data_text = self.random.process(data_text)
        data_text = self.variable.process(data_text)
        data_text = self.table_handler.process(data_text)
        data_structure = self.get_data_structure(data_text)
        return data_structure


    def get_data_structure(self,solved_table):
        temp = {}
        pattern = r'(\$\w+)\s*=\s*([^;]+);'
        matches = re.findall(pattern,solved_table)
        for match in matches:
            try:
                temp[match[0]] = eval(match[1])
            except:
                temp[match[0]] = match[1]

        return temp
    def set_calculator(self,calculator):
        self.calculator = calculator



    def set_random(self,random):
        self.random = random


    def set_variable(self,variable):
        self.variable = variable


    def set_table_handler(self,table_handler):
        self.table_handler = table_handler



##
##data = DataStructure()
##variable = '''
##$x = 1;
##$y = cal(1+2);
##$table = [{"age" : 21}, {"age" : 20}];
##$table2 = $<table>(x)=>{ x.age};
##'''
##print(data.run(variable))
