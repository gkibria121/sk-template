import regex as re
from .wrapper.sk_mongo_wrapper.sk_mongo_wrapper import MongoWrapper
from .controller.sk_mongo_controller.sk_mongo_controller import MongoController
from .process.create_declaration_list import CreateDeclarationText
from .process.get_variable_tokens import GetVariableTokens
from .process.solve_table import SolveTable
from .process.single_table_solver import SingleTableSolver

class TableHandler:

    def __init__(self):
        self.data = {}
        self.create_declaration_text = CreateDeclarationText()
        self.get_variable_tokens= GetVariableTokens()
        self.solve_table = SolveTable()
        self.single_table_solver = SingleTableSolver()
        self.single_table_solver.set_wrapper(MongoWrapper())
        self.single_table_solver.set_mongo_controller(MongoController())
        self.solve_table.set_single_table_solver(self.single_table_solver)


    def process(self,variable_declarations):
        variable_tokens = self.get_variable_tokens.run(variable_declarations)

        declaration_list = self.solve_table.run(variable_tokens)
        declaration_text = self.create_declaration_text.run(declaration_list)

        return declaration_text





##$table4 = $<table,table3,table2>(x,z:x.number==z.number,y:x.number==y.number)=>{ {'name' : x.item , 'cost' : x.quantity*y.price ,'unit' : x.unit} };
##$table2 = $<table>(x)=>{ {'number' : $<table><[$parent_index-1].number|1>+$<table><[$parent_index+1].number|1> } };

##        $table4 = $<table1:x,table2:y,table3:z>join(y:y.item=x.item,z_:x.item=z.item)->where( ((x.item == x.item $or y.item!=x.item) $and (x.item!=y.item )) $or x.item == y.item );
##        $table4 = $<table1:x>group(x.age,x.name)->select({ 'totalId' : {'$sum' : "$y.id"}, 'name' : '$name' , 'age' : '$age' });
##        $table4 = $<table1:x>sort(x.name=1,x.name=-1);
##        $table4 = $<table1:x>sort(x.y.id=-1,x.name=-1);
variables = '''
        $table1 = [{'item' : 'apple' , 'price' : 100, 'quantity' : 20},{'item' : 'apple' , 'price' : 200, 'quantity' : 40},{'item' : 'apple' , 'price' : 300, 'quantity' : 50},{'item' : 'apple' , 'price' : 400, 'quantity' : 60},{'item' : 'banana' , 'price' : 200, 'quantity' : 30}];

        $table5 = $<table1:x>group(x.item)->select({'item' : x.item ,'price' : addToSet(x.price)});


        '''

##
##table = TableHandler()
##
##print(table.process(variables))
##


