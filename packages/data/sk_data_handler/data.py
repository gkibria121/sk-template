import regex as re
from .comment_remover import CommentRemover
class DataStructure:
    def __init__(self):
        self.random = None
        self.variable = None
        self.table = None
        self.comment_remover = CommentRemover()
        self.json_process = JsonProcess()


    def run(self,data_text):
        self.comment_remover.set_next(self.json_process)
        self.json_process.set_next(self.random)
        self.random.set_next(self.variable)
        self.variable.set_next(self.table_handler)
        self.table_handler.set_next(type('Default',(),{'process' : lambda value: value}))


        data_text = self.comment_remover.process(data_text)
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


class JsonProcess:
    def process(self,text):

        text =re.sub(r'(\{([^{}]|(?1))*\})',lambda match:self.process_key(match[0]),text )
        print(text)

        return self.go_next.process(text)
    def process_key(self,json_data):

        return re.sub(r'(?![\"\'])([^\"\'\s\,\{\}]+)(?![\"\'])\s*\:',lambda match: f'"{match[1]}" :',json_data)

    def set_next(self,go_next):
        self.go_next= go_next

##
##data = DataStructure()
##variable = '''
##$x = 1;
##$y = cal(1+2);
##$table = [{"age" : 21}, {"age" : 20}];
##$table2 = $<table>(x)=>{ x.age};
##'''
##print(data.run(variable))
