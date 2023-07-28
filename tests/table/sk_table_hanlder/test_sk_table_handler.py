from sk_table_hanlder import TableHandler
import unittest

class TestTableHandler(unittest.TestCase):
    def setUp(self):
        self.table_hanlder = TableHandler()

    def test_table_hanlder(self):
        variables = '''
        $table= [{"age" : 20},{"age" : 22}];
        $table2 = $table(x)=>(x.age>10){ 1 };
        '''
        resutl = self.table_hanlder.run(variables)

        self.assertEqual(resutl,'''
        $table= [{"age" : 20},{"age" : 22}];
        $table2 = [1, 1];
        ''')

        variables = '''
        $table= [{"age" : 20},{"age" : 22}];
        $table2 = $table(x)=>(x.age>10){ $index };
        '''
        resutl = self.table_hanlder.run(variables)
        self.assertEqual(resutl,'''
        $table= [{"age" : 20},{"age" : 22}];
        $table2 = [0, 1];
        ''')

        variables = '''
        $table= [{"radius" : 10},{"radius" : 100}];
        $table2 = $table(x)=>(x.radius>10){ {'area' : x.radius*x.radius*3.1416 , 'radius' : x.radius , 'increasing_number' : x.radius+$table2<[$index-1].radius|0> } };
        '''
        resutl = self.table_hanlder.run(variables)
        self.assertEqual(resutl,'''
        $table= [{"radius" : 10},{"radius" : 100}];
        $table2 = [{'area': 31416.0, 'radius': 100, 'increasing_number': 100}];
        ''')


        variables = '''
        $table= [{"radius" : 10},{"radius" : 100}];
        $table2 = $table(x)=>(x.radius>9){ {'area' : x.radius*x.radius*3.1416 , 'radius' : x.radius , 'increasing_number' : x.radius+$table2<[$index-1].radius|0> } };
        '''
        resutl = self.table_hanlder.run(variables)
        self.assertEqual(resutl,'''
        $table= [{"radius" : 10},{"radius" : 100}];
        $table2 = [{'area': 314.15999999999997, 'radius': 10, 'increasing_number': 10}, {'area': 31416.0, 'radius': 100, 'increasing_number': 110}];
        ''')

if __name__=='__main__':
    unittest.main()
