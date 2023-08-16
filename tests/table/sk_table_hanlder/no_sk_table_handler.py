from sk_table_hanlder import TableHandler
import unittest

class TestTableHandler(unittest.TestCase):
    def setUp(self):
        self.table_hanlder = TableHandler()

    def test_table_hanlder(self):


        variables = '''
        $table= [{"age" : 20},{"age" : 22}];
        $table2 = $<table>(x)=>(x.age>10){ x.index };
        '''
        resutl = self.table_hanlder.process(variables)
        self.assertEqual(resutl,'''$table = [{'age': 20}, {'age': 22}];
$table2 = [0, 1];
''')

        variables = '''
        $table= [{"radius" : 10},{"radius" : 100}];
        $table2 = $<table>(x)=>(x.radius>10){ {'area' : x.radius*x.radius*3.1416 , 'radius' : x.radius , 'increasing_number' : x.radius+$<table2><[x.index-1].radius|0> } };
        '''
        resutl = self.table_hanlder.process(variables)
        self.assertEqual(resutl,'''$table = [{'radius': 10}, {'radius': 100}];
$table2 = [{'area': 31416.0, 'radius': 100, 'increasing_number': 100}];
''')


        variables = '''
        $table= [{"radius" : 10},{"radius" : 100}];
        $table2 = $<table>(x)=>(x.radius>9){ {'area' : x.radius*x.radius*3.1416 , 'radius' : x.radius , 'increasing_number' : x.radius+$<table2><[x.index-1].radius|0> } };
        '''
        resutl = self.table_hanlder.process(variables)
        self.assertEqual(resutl,'''$table = [{'radius': 10}, {'radius': 100}];
$table2 = [{'area': 314.15999999999997, 'radius': 10, 'increasing_number': 10}, {'area': 31416.0, 'radius': 100, 'increasing_number': 110}];
''')

    def test_table_hanlder_with_mass_data(self):
        variables = '''
        $table= [{"name": "John Doe","age": 20,"roll": "1001","gpa": 3.5},{"name": "Jane Smith","age": 19,"roll": "1002","gpa": 3.9},{"name": "Michael Johnson","age": 21,"roll": "1003","gpa": 3.2},{"name": "Emily Brown","age": 18,"roll": "1004","gpa": 3.8},{"name": "William Lee","age": 20,"roll": "1005","gpa": 3.6},{"name": "Sophia Kim","age": 19,"roll": "1006", "gpa": 3.7}];
        $table2 = $<table>(x)=>(x.age>=20){ {"name" : x.name ,"age" : x.age, "age_gpa" : x.age*x.gpa, "increased_gpa" : x.gpa +$table2<[x.index-1].gpa|0> , "gpa" : x.gpa} };'''
        result = self.table_hanlder.process(variables)
        self.maxDiff = None
        self.assertEqual(result,'''$table = [{'name': 'John Doe', 'age': 20, 'roll': '1001', 'gpa': 3.5}, {'name': 'Jane Smith', 'age': 19, 'roll': '1002', 'gpa': 3.9}, {'name': 'Michael Johnson', 'age': 21, 'roll': '1003', 'gpa': 3.2}, {'name': 'Emily Brown', 'age': 18, 'roll': '1004', 'gpa': 3.8}, {'name': 'William Lee', 'age': 20, 'roll': '1005', 'gpa': 3.6}, {'name': 'Sophia Kim', 'age': 19, 'roll': '1006', 'gpa': 3.7}];
$table2 = [{'name': 'John Doe', 'age': 20, 'age_gpa': 70.0, 'increased_gpa': 3.5, 'gpa': 3.5}, {'name': 'Michael Johnson', 'age': 21, 'age_gpa': 67.2, 'increased_gpa': 6.7, 'gpa': 3.2}, {'name': 'William Lee', 'age': 20, 'age_gpa': 72.0, 'increased_gpa': 6.800000000000001, 'gpa': 3.6}];
''')

    def test_cumulative(self):
        variables = '''
        $table= [{'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}];
        $table2 = $<table>(x)=>{ {'number' : x.number , 'cumulitive' : x.number+$<table2><[x.index-1].cumulitive|0>} };'''
        result = self.table_hanlder.process(variables)
        self.maxDiff = None
        self.assertEqual(result,'''$table = [{'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}, {'number': 1}];
$table2 = [{'number': 1, 'cumulitive': 1}, {'number': 1, 'cumulitive': 2}, {'number': 1, 'cumulitive': 3}, {'number': 1, 'cumulitive': 4}, {'number': 1, 'cumulitive': 5}, {'number': 1, 'cumulitive': 6}, {'number': 1, 'cumulitive': 7}, {'number': 1, 'cumulitive': 8}, {'number': 1, 'cumulitive': 9}, {'number': 1, 'cumulitive': 10}, {'number': 1, 'cumulitive': 11}, {'number': 1, 'cumulitive': 12}, {'number': 1, 'cumulitive': 13}, {'number': 1, 'cumulitive': 14}, {'number': 1, 'cumulitive': 15}, {'number': 1, 'cumulitive': 16}, {'number': 1, 'cumulitive': 17}, {'number': 1, 'cumulitive': 18}, {'number': 1, 'cumulitive': 19}, {'number': 1, 'cumulitive': 20}, {'number': 1, 'cumulitive': 21}, {'number': 1, 'cumulitive': 22}, {'number': 1, 'cumulitive': 23}, {'number': 1, 'cumulitive': 24}, {'number': 1, 'cumulitive': 25}, {'number': 1, 'cumulitive': 26}, {'number': 1, 'cumulitive': 27}, {'number': 1, 'cumulitive': 28}, {'number': 1, 'cumulitive': 29}, {'number': 1, 'cumulitive': 30}, {'number': 1, 'cumulitive': 31}, {'number': 1, 'cumulitive': 32}, {'number': 1, 'cumulitive': 33}, {'number': 1, 'cumulitive': 34}, {'number': 1, 'cumulitive': 35}, {'number': 1, 'cumulitive': 36}, {'number': 1, 'cumulitive': 37}, {'number': 1, 'cumulitive': 38}, {'number': 1, 'cumulitive': 39}, {'number': 1, 'cumulitive': 40}, {'number': 1, 'cumulitive': 41}, {'number': 1, 'cumulitive': 42}, {'number': 1, 'cumulitive': 43}, {'number': 1, 'cumulitive': 44}, {'number': 1, 'cumulitive': 45}, {'number': 1, 'cumulitive': 46}, {'number': 1, 'cumulitive': 47}, {'number': 1, 'cumulitive': 48}, {'number': 1, 'cumulitive': 49}, {'number': 1, 'cumulitive': 50}, {'number': 1, 'cumulitive': 51}, {'number': 1, 'cumulitive': 52}, {'number': 1, 'cumulitive': 53}, {'number': 1, 'cumulitive': 54}, {'number': 1, 'cumulitive': 55}, {'number': 1, 'cumulitive': 56}, {'number': 1, 'cumulitive': 57}, {'number': 1, 'cumulitive': 58}, {'number': 1, 'cumulitive': 59}, {'number': 1, 'cumulitive': 60}, {'number': 1, 'cumulitive': 61}, {'number': 1, 'cumulitive': 62}, {'number': 1, 'cumulitive': 63}, {'number': 1, 'cumulitive': 64}, {'number': 1, 'cumulitive': 65}, {'number': 1, 'cumulitive': 66}, {'number': 1, 'cumulitive': 67}, {'number': 1, 'cumulitive': 68}, {'number': 1, 'cumulitive': 69}, {'number': 1, 'cumulitive': 70}, {'number': 1, 'cumulitive': 71}, {'number': 1, 'cumulitive': 72}, {'number': 1, 'cumulitive': 73}, {'number': 1, 'cumulitive': 74}, {'number': 1, 'cumulitive': 75}, {'number': 1, 'cumulitive': 76}, {'number': 1, 'cumulitive': 77}, {'number': 1, 'cumulitive': 78}, {'number': 1, 'cumulitive': 79}, {'number': 1, 'cumulitive': 80}, {'number': 1, 'cumulitive': 81}, {'number': 1, 'cumulitive': 82}, {'number': 1, 'cumulitive': 83}, {'number': 1, 'cumulitive': 84}, {'number': 1, 'cumulitive': 85}, {'number': 1, 'cumulitive': 86}, {'number': 1, 'cumulitive': 87}, {'number': 1, 'cumulitive': 88}, {'number': 1, 'cumulitive': 89}, {'number': 1, 'cumulitive': 90}, {'number': 1, 'cumulitive': 91}, {'number': 1, 'cumulitive': 92}, {'number': 1, 'cumulitive': 93}, {'number': 1, 'cumulitive': 94}, {'number': 1, 'cumulitive': 95}, {'number': 1, 'cumulitive': 96}, {'number': 1, 'cumulitive': 97}, {'number': 1, 'cumulitive': 98}, {'number': 1, 'cumulitive': 99}, {'number': 1, 'cumulitive': 100}, {'number': 1, 'cumulitive': 101}];
''')
    def test_previous_next_sum(self):
        variables = '''
        $table= [{'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}];
        $table2 = $<table>(x)=>{ {'number' : $<table><[x.loop_index-1].number|1>+$table<[x.loop_index+1].number|1> } };'''
        result = self.table_hanlder.process(variables)
        self.maxDiff = None
        self.assertEqual(result,'''$table = [{'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}, {'number': 1}, {'number': 0}];
$table2 = [{'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}, {'number': 0}, {'number': 2}];
''')


    def  test_create_table_with_lookup_table(self):

        variables = '''
        $table1 = [{'item' : 'mobile'},{'item' : 'apple'}];
        $table2 = [{'item' : 'mobile','quantity' : 10},{'item' : 'apple','quantity' : 20}];
        $table3 = [{'item' : 'mobile','price' : 100},{'item' : 'apple','price' : 50}];
        $table4 = $<table1,table2,table3>(x,y:y.item==x.item,z:z.item==x.item)=>{ {'item' : x.item,'cost' : y.quantity*z.price } };
        $table4 = $<table1,table2,table3>(x,y:y.item==x.item,z:z.item==x.item)=>{ {'item' : x.item,'cost' : y[0].quantity*z[0].price } };
        '''
        result = self.table_hanlder.process(variables)
        self.maxDiff = None
        self.assertEqual(result,'''$table1 = [{'item': 'mobile'}, {'item': 'apple'}];
$table2 = [{'item': 'mobile', 'quantity': 10}, {'item': 'apple', 'quantity': 20}];
$table3 = [{'item': 'mobile', 'price': 100}, {'item': 'apple', 'price': 50}];
$table4 = [{'item': 'mobile', 'cost': 1000}, {'item': 'apple', 'cost': 1000}];
''')
    def  test_create_table_with_lookup_table(self):

        variables = '''
        $table2 = [{'item' : 'mobile','quantity' : 10},{'item' : 'apple','quantity' : 20}];
        $table3 = [{'item' : 'mobile','price' : 100},{'item' : 'apple','price' : 50}];
        $table4 = $<table2,table3>(x,y:y.item==x.item)=>{ {'item' : x.item,'cost' : x.quantity*y[0].price } };
        '''
        result = self.table_hanlder.process(variables)
        self.maxDiff = None
        self.assertEqual(result,'''$table2 = [{'item': 'mobile', 'quantity': 10}, {'item': 'apple', 'quantity': 20}];
$table3 = [{'item': 'mobile', 'price': 100}, {'item': 'apple', 'price': 50}];
$table4 = [{'item': 'mobile', 'cost': 1000}, {'item': 'apple', 'cost': 1000}];
''')
    def  no_test_create_table_with_lookup_table(self):

        variables = '''
        $table2 = [{'party' : 'x'},{'party' : 'y'}];
        $table3 = [{'party' : 'x' , 'paid' : 10},{'party' : 'x' , 'paid' : 10},{'party' : 'y' , 'paid' : 30},{'party' : 'y' , 'paid' : 20}];
        $table4 = $<table2,table3>(x,y:y.party==x.party)=>{ {'party' : x.party,'sum' : y.paid.sum() } };
        '''
        result = self.table_hanlder.process(variables)
        self.maxDiff = None
        self.assertEqual(result,'''$table1 = [{'item': 'mobile'}, {'item': 'apple'}];
$table2 = [{'item': 'mobile', 'quantity': 10}, {'item': 'apple', 'quantity': 20}];
$table3 = [{'item': 'mobile', 'price': 100}, {'item': 'apple', 'price': 50}];
$table4 = [{'item': 'mobile', 'cost': 1000}, {'item': 'apple', 'cost': 1000}];
''')




if __name__=='__main__':
    unittest.main()


