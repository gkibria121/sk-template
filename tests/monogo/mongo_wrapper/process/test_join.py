import unittest
from sk_mongo_wrapper.process.join import JoinProcess
from sk_mongo_wrapper.query_process import ArgumentProcess
class TestJoinProcess(unittest.TestCase):

    def setUp(self):
        self.join_process = JoinProcess()
        self.argument_process = ArgumentProcess()
        self.join_process.set_argument_process(self.argument_process)
        self.join_process.set_next(type('Default',(),{'process' : lambda name,argument: (name,argument)}))


##    def test_join_process_empty(self):
##        name = 'join'
##        argument = ''
##        result = self.join_process.process(name,argument)
##        self.assertEqual(result,('join',[])) #[('from','as','foreign_id','local_id')]

    def test_join_process_empty(self):
        name = 'join'
        argument = 'z:x.item=y.item'
        self.argument_process.set_primary_table('x')
        self.join_process.set_primary_table('x')
        result = self.join_process.process(name,argument)
        self.assertEqual(result,('join',[('y', 'z', 'item', 'item')]))
    def test_join_process_empty(self):
        name = 'join'
        argument = 'z:x.item=y.item,a:x.item=z.item'
        self.argument_process.set_primary_table('x')
        self.join_process.set_primary_table('x')

        result = self.join_process.process(name,argument)
        self.assertEqual(result,('join',[('y', 'z', 'item', 'item'), ('z', 'a', 'item', 'item')]))

if __name__=="__main__":
    unittest.main()

