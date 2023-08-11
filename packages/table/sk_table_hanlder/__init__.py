import regex as re
from wrapper.sk_mongo_wrapper.sk_mongo_wrapper import MongoWrapper
from controller.sk_mongo_controller.sk_mongo_controller import MongoController
class TableHandler:

    def __init__(self):
        self.data = {}
        self.create_declaration_text = CreateDeclarationText()
        self.get_variable_tokens= GetVariableTokens()
        self.solve_table = SolveTable()


    def process(self,variable_declarations):
        variable_tokens = self.get_variable_tokens.run(variable_declarations)

        declaration_list = self.solve_table.run(variable_tokens)
        declaration_text = self.create_declaration_text.run(declaration_list)

        return declaration_text





class CreateDeclarationText:
    def run(self,declaration_list):
        declaration_text = ''
        for key,value in declaration_list.items():
            declaration_text+= f'{key} = {value};\n'

        return declaration_text

class GetVariableTokens:
    def run(self,declarations):
        pattern = r'(\$\w+\s*=\s*[^;]+);'
        tokens = [self.get_key_value(item) for index,item in enumerate( re.split(pattern,declarations)) if item !='' and item !='\n']
        tokens = [item for index,item in enumerate(tokens) if item !=None ]

        return tokens

    def get_key_value(self,item):
        pattern = r'(\$\w+)\s*=([^;]+)'
        if len(re.findall(pattern,item))>0:
            return re.findall(pattern,item)[0]



class SolveTable:
    def __init__(self):
        self.single_table_solver =SingleTableSolver()
    def run(self,variable_tokens):
        temp_data = {}

        for variable in variable_tokens:
            if '$' not in variable[1]:
                temp_data.update({variable[0]: eval(variable[1])})
            else:
                value =self.single_table_solver.run(temp_data,variable)
                temp_data.update({variable[0] : value} )

        return temp_data

class SingleTableSolver:
    def __init__(self):
        self.wrapper = MongoWrapper()
        self.wrapper.set_mongo_controller(MongoController())

    def run(self,data,variable):
        variable_name = variable[0]
        table_expression = variable[1]
        pattern = r'\$<((\w+(\:\w+))(,(\w+(\:\w+)))*)>((\w+(\((([^()]|(?9)))*\)))(->(\w+(\((([^()]|(?9)))*\))))*)'
        match = re.search(pattern , table_expression)
        if match:
            table_names = [item for index,item in enumerate(match[1].split(',')) if item !='']
            self.wrapper.set_table_data(data,table_names)
            table_queries = self.get_query_list(match[7])

            queries = self.wrapper.process_queries(table_queries)

            script = self.wrapper.query(queries)

            result = self.wrapper.evaluate(script)

            return result

        return -1

    def get_query_list(self,queries):

        queries = [item for index,item in enumerate( re.split(r'->',queries)) if item!='']

        return queries




##$table4 = $<table,table3,table2>(x,z:x.number==z.number,y:x.number==y.number)=>{ {'name' : x.item , 'cost' : x.quantity*y.price ,'unit' : x.unit} };
##$table2 = $<table>(x)=>{ {'number' : $<table><[$parent_index-1].number|1>+$<table><[$parent_index+1].number|1> } };
##        $table4 = $<table2:x,table3:y>join(y.age=x.item,z.quantity=x.item)->where(x.quantity > 10 and x.item=3)->select({'item' : x.item,'stock' : y.stock_in.sum()-y.stcok_out.sum() });

variables = '''
        $table1 = [{'item' : 'mobile'},{'item' : 'apple'}];
        $table2 = [{'item' : 'mobile','quantity' : 10},{'item' : 'apple','quantity' : 20}];
        $table3 = [{'item' : 'mobile','price' : 100},{'item' : 'apple','price' : 50}];
        $table4 = $<table1:x,table2:y,table3:z>join(y:y.item=x.item,z:x.item=z.item);
        '''


table = TableHandler()

print(table.process(variables))



