import regex as re

class TableHandler:

    def __init__(self):
        self.data = {}

    def get_data(self,variable_declarations):
        data = {}
        pattern = '(\$\w+)\s*=\s*([^=;]+)\;'
        matches = re.findall(pattern,variable_declarations)
        for variable,value in matches:
            data[variable] = eval(value)
        return data

    def solve_table(self,data,declarations):
        pattern = r'((\$\w+)\s*\((\w+)\)\s*=>\s*(\((.*?)\))?\s*(\{(([^{}]|(?6))*)\}))'

        matches = re.findall(pattern,declarations)
        replace = ''
        for match in matches:
            replace = match[0]

            variable = match[1]
            placeholder = match[2]
            condition = match[4]
            return_value =  match[6]

            value = self.get_table_value(data,variable,placeholder,condition,return_value)

            declarations = re.sub(re.escape(replace),value,declarations)

        return declarations


    def run(self,variable_declarations):

        data = self.get_data(variable_declarations)


        declaration_text = self.solve_table(data,variable_declarations)


        return declaration_text


    def get_table_value(self,data,variable,placeholder,condition,return_value):

        data = data[variable]

        for index,value in enumerate(data):
            exec(f"{placeholder} = value")



        return return_value










table_text = '''
$x = "hi there";
$table = [{"name" : "kibria", "age" : 23},{"name" : "mehedi", "age" : 23}];
$table2 = $table(x) => (x.radius>2) {  { 'radius' : x.radius , 'area' : x.radius*radius*3.1416, 'sum' : x+$table[index-1,-1]} };
'''

table = TableHandler()

print(table.run(table_text))



