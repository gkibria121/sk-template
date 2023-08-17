import unittest
from sk_mongo_wrapper.process.order_by import OrderByProcess
from sk_mongo_wrapper.process.order_by import SortObject
from sk_mongo_wrapper.process.order_by import GetOrder
from sk_mongo_wrapper.query_process import ArgumentProcess


class TestSortProcess(unittest.TestCase):

    def setUp(self):
        self.sort_process = OrderByProcess()
        self.sort_process.set_next(type('Default',(),{'process' : lambda name,argument: (name,argument)}))
        self.argument_process =ArgumentProcess()
        self.sort_process.set_argument_process(self.argument_process)


##    def test_sort_process_empty(self):
##        name = 'sort'
##        argument = ''
##        self.argument_process.set_primary_table('x')
##        result = self.sort_process.process(name,argument)
##        self.assertEqual(result,('sort', {'': 1})) #{'sort_by' : 'asc/des'}


    def test_sort_process(self):
        name = 'sort'
        argument = 'x.item'
        self.argument_process.set_primary_table('x')
        result = self.sort_process.process(name,argument)
        self.assertEqual(result,('sort', {'item': 1}))


        name = 'sort'
        argument = 'x.item,y.item'
        self.argument_process.set_primary_table('x')
        result = self.sort_process.process(name,argument)
        self.assertEqual(result,('sort', {'item': 1, 'y.item':1}))

        name = 'sort'
        argument = 'x.item:des'
        self.argument_process.set_primary_table('x')
        result = self.sort_process.process(name,argument)
        self.assertEqual(result,('sort', {'item': -1}))

        name = 'sort'
        argument = 'x.item:des,y.item'
        self.argument_process.set_primary_table('x')
        result = self.sort_process.process(name,argument)
        self.assertEqual(result,('sort', {'item':-1, 'y.item': 1}))


        name = 'sort'
        argument = 'x.item:des,y.item:des'
        self.argument_process.set_primary_table('x')
        result = self.sort_process.process(name,argument)
        self.assertEqual(result,('sort', {'item': -1, 'y.item': -1}))


        name = 'sort'
        argument = 'x.item:asc,y.item:asc'
        self.argument_process.set_primary_table('x')
        result = self.sort_process.process(name,argument)
        self.assertEqual(result,('sort', {'item': 1, 'y.item': 1}))



class TestSortObject(unittest.TestCase):

    def setUp(self):
        self.sort_object = SortObject()
        self.argument_process =ArgumentProcess()
        self.sort_object.set_argument_process(self.argument_process)

    def test_sort_process(self):
        argument = ['x.item:asc','y.item:asc']
        self.argument_process.set_primary_table('x')
        result = self.sort_object.process(argument)
        self.assertEqual(result,{'item': 1, 'y.item': 1})

    def test_sort_process(self):
        argument = ['x.item','y.item']
        self.argument_process.set_primary_table('x')
        result = self.sort_object.process(argument)
        self.assertEqual(result,{'item': 1, 'y.item': 1})
    def test_sort_process(self):
        argument = ['x.item:des','y.item']
        self.argument_process.set_primary_table('x')
        result = self.sort_object.process(argument)
        self.assertEqual(result,{'item': -1, 'y.item': 1})

    def test_sort_process(self):

        argument = ['x.item:des','y.item:des']
        self.argument_process.set_primary_table('x')
        result = self.sort_object.process(argument)
        self.assertEqual(result,{'item': -1, 'y.item': -1})
    def test_sort_process(self):

        argument = ['x.item:asc','y.item:des']
        self.argument_process.set_primary_table('x')
        result = self.sort_object.process(argument)
        self.assertEqual(result,{'item': 1, 'y.item': -1})




class TestGetOrder(unittest.TestCase):

    def setUp(self):
        self.get_order = GetOrder()



    def test_get_order(self):

       self.assertEqual(self.get_order.run('asc'),1)
       self.assertEqual(self.get_order.run('a'),1)
       self.assertEqual(self.get_order.run('1'),1)
       self.assertEqual(self.get_order.run(1),1)


       self.assertEqual(self.get_order.run('des'),-1)
       self.assertEqual(self.get_order.run('d'),-1)
       self.assertEqual(self.get_order.run('-1'),-1)
       self.assertEqual(self.get_order.run(-1),-1)




if __name__=="__main__":
    unittest.main()

