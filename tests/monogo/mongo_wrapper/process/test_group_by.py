import unittest
from sk_mongo_wrapper.process.group_by import GroupByProcess
from sk_mongo_wrapper.query_process import ArgumentProcess


class TestGroup(unittest.TestCase):

    def setUp(self):
        self.group_by_process = GroupByProcess()
        self.argument_process = ArgumentProcess()
        self.group_by_process.set_argument_process(self.argument_process)
        self.group_by_process.set_next(type('Default',(),{'process' : lambda name,argument: (name,argument)}))

    def test_group_by(self):
        self.argument_process.set_primary_table('x')

        result = self.group_by_process.process('group','x.item')
        self.assertEqual(result,('group' , {'_id': {'item': '$item'}}))


        self.argument_process.set_primary_table('x')

        result = self.group_by_process.process('group','x.item,x.y.item')
        self.assertEqual(result,('group' , {'_id': {'item': '$item', 'y.item': '$y.item'}}))


        self.argument_process.set_primary_table('x')

        result = self.group_by_process.process('group','x.item,x.y.item,z.item')
        self.assertEqual(result,('group' , {'_id': {'item': '$item', 'y.item': '$y.item', 'z.item': '$z.item'}}))


        self.argument_process.set_primary_table('x')

        result = self.group_by_process.process('group','x.item,x.y.item')
        self.assertEqual(result,('group' ,{'_id': {'item': '$item', 'y.item': '$y.item'}}))


if __name__=="__main__":
    unittest.main()

