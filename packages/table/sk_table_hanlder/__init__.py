import regex as re

class TableHandler:

    def __init__(self):
        self.data = {}

    def get_data(self,variable_declarations):
        data = {}
        pattern = '(\$\w+)\s*=\s*([^=;]+)\;'
        matches = re.findall(pattern,variable_declarations)
        for variable,value in matches:
            data[variable] = eval(value) if 'eval' not in value else value
        return data

    def solve_table(self,data,declarations):
        pattern = r'(\$\w+)\s*=\s*((\$\w+)\s*\((\w+)\)\s*=>\s*(\((.*?)\))?\s*(\{(([^{}]|(?7))*)\}))'

        matches = re.findall(pattern,declarations)
        replace = ''
        for match in matches:
            replace = match[1]

            variable = match[0]
            template_variable = match[2]
            placeholder = match[3]
            condition = match[5]
            return_value =  match[7]

            value = self.get_table_value(data,template_variable,variable,placeholder,condition,return_value)

            declarations = re.sub(re.escape(replace),str(value),declarations)

        return declarations


    def process(self,variable_declarations):

        procced_table = self.process_table(variable_declarations)

        data = self.get_data(variable_declarations)


        declaration_text = self.solve_table(data,procced_table)


        return declaration_text


    def get_table_value(self,data_stucture,template_variable,variable,placeholder,condition,return_value):

        data = data_stucture[template_variable]

        result = []

        condition = self.index_process(condition)
        data_stucture.update({variable : []})
        index = 0
        list_len = len(data)

        for parent_index,value in enumerate(data):

            exec(f"{placeholder} = value")
            if condition =='' or eval(f"{condition}"):
                item =return_value
                item = self.index_process(item)
                item = self.process_ref(item,index,parent_index,list_len)
                item = self.put_value(data_stucture,item)

                item = eval(item) if 'eval' not in item else item
                result.append(item)
                data_stucture.update({variable : result})
                index = index+1


        return result

    def index_process(self,code):

        pattern =r'(?:\.([^\d][\w]*))\b(?!\()'

        code = re.sub(pattern, lambda match: f'["{match.group(1)}"]', code)
        return code

    def put_value(self,data_structure,item):

        for key,value in data_structure.items():

            item = re.sub(re.escape(key)+r'\b',str(value),item)

        return item

    def process_ref(self,item,index,parent_index,list_len):

        item = re.sub(r'\$index\b',str(index),item)
        item = re.sub(r'\$parent_index\b',str(index),item)
        pattern = r'((\$[^$]+)?(\<([^|]+)\|([^|]+)\>))'
        item = re.sub(pattern, lambda match: f"{match.group(2)}{match.group(4)}" if  self.index_validation(match.group(4),list_len)  else f"{match.group(5)}", item)

        return item

    def index_validation(self,text,list_len):
        pattern = r'\[([^\[\]]+)\]'
        matches = re.findall(pattern,text)
        for match in matches:
            if eval(f"type({match})==int and ({match}<=-1 or {match}>={list_len})"):
                return False
        return True

    def process_table(self,declarations):
        declarations  = re.sub(r'(\$)<(\w+)>',lambda catch: catch[1]+catch[2],declarations)
        return declarations
##$table3 = $<table1,table2>(x,y:x.item=y.item)=>{ 'name' : x.item , 'cost' : x.quantity*y.price ,'unit' : x.unit };

##
##variables = '''
##        $table= [{'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}];
##        $table2 = $<table>(x)=>{ {'number' : $table<[$parent_index-1].number|1>+$table<[$parent_index+1].number|1> } };'''
##table = TableHandler()
##
##print(table.process(variables))



