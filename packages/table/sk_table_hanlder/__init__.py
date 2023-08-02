import regex as re

class TableHandler:

    def __init__(self):
        self.data = {}

    def get_data(self,data_structure,tables):
        data = {}
        for table in tables:
            data[table] = data_structure[table]
        return data

    def solve_table(self,variable_tokens):

        temp_data = {}

        for variable in variable_tokens:
            if '$' not in variable[1]:
                temp_data.update({variable[0]: eval(variable[1])})
            else:
                value =self.solve_single_table(temp_data,variable)
                temp_data.update({variable[0] : value} )

        return temp_data

    def solve_single_table(self,data,variable):

        pattern = r'\$<((\w+)(,\w+)*)>(\(((\w+)(,\w+\:[^,)]+)*)\))=>(\((([^()]|(?8))*)\))?(\{(([^{}]|(?11))*)\})'
        match = re.search(pattern,variable[1])
        if match:
            working_table = variable[0]
            tables = [f'${item}' for index,item in enumerate(re.split(r',',match[1])) if item!='' and item!='\n']
            parent_table = f"${match[2]}"
            lookup_conditions = match[5]
            condition = match[9]
            return_data = match[12]
            value = self.get_table_value(data,tables,parent_table,lookup_conditions,condition,return_data,working_table)
            return value

        return





    def process(self,variable_declarations):
        variable_tokens = self.get_variable_tokens(variable_declarations)

        declaration_list = self.solve_table(variable_tokens)
        declaration_text = self.create_declaration_text(declaration_list)




        return declaration_text


    def create_declaration_text(self,declaration_list):
        declaration_text = ''
        for key,value in declaration_list.items():
            declaration_text+= f'{key} = {value};'

        return declaration_text



    def get_variable_tokens(self,declarations):


        pattern = r'(\$\w+\s*=\s*[^;]+);'
        tokens = [self.get_key_value(item) for index,item in enumerate( re.split(pattern,declarations)) if item !='' and item !='\n']
        tokens = [item for index,item in enumerate(tokens) if item !=None ]

        return tokens



    def get_table_value(self,data,tables,parent_table,lookup_conditions,condition,return_data,working_table):
        data_structure = data
        data_structure.update({working_table : []})
        data = self.get_data(data,tables)
        parent_data = data[parent_table]
        lookup_tables = tables[1:]
        parent_table_placeholer = re.search(r'(\w+)(?!\:|\.)',lookup_conditions)[1]
        lookup_table_placeholer_with_condition = re.findall(r'(\w+)\:([^,]+)',lookup_conditions)


        temp = []
        index = 0
        loop_index = 0
        while loop_index<len(parent_data):

            parent_data[loop_index].update({'index' : index,'loop_index' : loop_index})

            exec(f"{parent_table_placeholer} = {parent_data[loop_index]}")
            index2= 0
            while index2<len(lookup_table_placeholer_with_condition):
                exec(f"{lookup_table_placeholer_with_condition[index2][0]} = self.get_lookup_placholder_value(data,lookup_tables[index2],lookup_table_placeholer_with_condition[index2],parent_table_placeholer,{parent_table_placeholer})")
                index2 = index2+1

            if condition==None or eval(self.index_process(condition)):

                value = self.index_process(return_data)
                value = self.table_process(value)
                value = self.process_ref(value,data_structure,parent_table_placeholer,parent_data[loop_index])
                value = self.put_value(data_structure,value)
                value =eval(value)
                temp.append(value)
                data_structure.update({working_table : temp})
                index += 1
            del parent_data[loop_index]['index']
            del parent_data[loop_index]['loop_index']

            loop_index +=1

        return temp

    def get_lookup_placholder_value(self,data,lookup_table_name,lookup_placholder_condition,parent_table_placeholder,parent_table_placeholder_value):

        table_data = data[lookup_table_name]
        temp = []
        for column in table_data:
            condition =  self.index_process(lookup_placholder_condition[1])
            condition = re.sub(r'(?=\b)'+re.escape(lookup_placholder_condition[0])+r'(?=\b)',str(column) ,condition)
            condition = re.sub(r'(?=\b)'+re.escape(parent_table_placeholder)+r'(?=\b)',str(parent_table_placeholder_value) ,condition)
            if eval(condition):
                temp+=[column]

        return temp


    def index_process(self,code):
        pattern =r'(?:\.([^\d][\w]*))\b(?!\()'
        code = re.sub(pattern, lambda match: f'["{match.group(1)}"]', code)
        return code


    def put_value(self,data_structure,item):

        for key,value in data_structure.items():
            item = re.sub(re.escape(key)+r'\b',str(value),item)
        return item


    def process_ref(self,item,data_structure,placholder,placholder_value):
        pattern = r'((\$[^$]+)?(\<([^|]+)\|([^|]+)\>))'
        item = re.sub(pattern, lambda match: f"{match.group(2)}{match.group(4)}" if  self.index_validation(data_structure,match[2],match[4],placholder,placholder_value)  else f"{match.group(5)}", item)
        return item

    def index_validation(self,data_structure,table,text,placholder,placholder_value):
        exec(f"{placholder}=placholder_value")
        pattern = r'(\[(([^\]\[]|(?1))*)\])'
        matches = re.findall(pattern,text)
        for match in matches:
            if eval(f"type({match[1]})==int and ({match[1]}<=-1 or {match[1]}>=len(data_structure[table]))"):
                return False
        return True

    def table_process(self,string):

        return re.sub(r'\$<(\w+)>',lambda match: '$'+match[1] ,string)



    def get_key_value(self,item):
        pattern = r'(\$\w+)\s*=([^;]+)'
        if len(re.findall(pattern,item))>0:
            return re.findall(pattern,item)[0]

##$table4 = $<table,table3,table2>(x,z:x.number==z.number,y:x.number==y.number)=>{ {'name' : x.item , 'cost' : x.quantity*y.price ,'unit' : x.unit} };
##$table2 = $<table>(x)=>{ {'number' : $<table><[$parent_index-1].number|1>+$<table><[$parent_index+1].number|1> } };

##variables ='''
##        $table= [{'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}];
##        $table2 = $<table>(x)=>{ {'number' : $<table><[x.loop_index-1].number|1>+$table<[x.loop_index+1].number|1> } };
##        '''
##
##
##table = TableHandler()
##
##print(table.process(variables))
##


