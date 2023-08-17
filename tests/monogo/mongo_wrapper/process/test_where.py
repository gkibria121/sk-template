import unittest
from sk_mongo_wrapper.process.where import WhereProcess
from sk_mongo_wrapper.query_process import ArgumentProcess
from sk_mongo_wrapper.process.where.comparison import Equal
from sk_mongo_wrapper.process.where.comparison import EqualTo
from sk_mongo_wrapper.process.where.comparison import GreaterThen
from sk_mongo_wrapper.process.where.comparison import GreaterThenEqual
from sk_mongo_wrapper.process.where.comparison import LessThen
from sk_mongo_wrapper.process.where.comparison import LessThenEqual
from sk_mongo_wrapper.process.where.comparison import NotEqual


from sk_mongo_wrapper.process.where.comparison import ProcessOperators


from sk_mongo_wrapper.process.where.logical import And
from sk_mongo_wrapper.process.where.logical import Or
from sk_mongo_wrapper.process.where.logical import Not
from sk_mongo_wrapper.process.where.logical import In
from sk_mongo_wrapper.process.where.logical import NotIn




class TestWhereProcess(unittest.TestCase):

    def setUp(self):
        self.where_process = WhereProcess()
        self.where_process.set_next(type('Default',(),{'process' : lambda name,argument: (name,argument)}))
        self.argument_process =ArgumentProcess()
        self.where_process.set_argument_process(self.argument_process)

    def test_where_process(self):

        name = 'where'
        argument = 'x.item>1'
        self.argument_process.set_primary_table('x')
        result = self.where_process.process(name,argument)
        self.assertEqual(result,(name,{'item': {'$gt': 1}}))

        argument = 'x.item<1'
        self.argument_process.set_primary_table('x')
        result = self.where_process.process(name,argument)
        self.assertEqual(result,(name,{'item': {'$lt': 1}}))
        name = 'where'
        argument = 'x.item>=1'
        self.argument_process.set_primary_table('x')
        result = self.where_process.process(name,argument)
        self.assertEqual(result,(name,{'item': {'$gte': 1}}))

        argument = 'x.item<=1'
        self.argument_process.set_primary_table('x')
        result = self.where_process.process(name,argument)
        self.assertEqual(result,(name,{'item': {'$lte': 1}}))

        argument = 'x.item<=x.y.item'
        self.argument_process.set_primary_table('x')
        result = self.where_process.process(name,argument)
        self.assertEqual(result,(name,{'item': {'$lte': '$y.item'}}))


class TestEqualTo(unittest.TestCase):

    def setUp(self):
        self.eq = EqualTo()
        self.eq.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))
    def test_equal(self):
        result =self.eq.process('x.item==x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$eq" : x.y.item   } }')

        result =self.eq.process('x.item==x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$eq" : x.y.item   } }')


        result =self.eq.process('z.x.item==x.y.item')
        self.assertEqual(result,'{ "z.x.item" : { "$eq" : x.y.item   } }')

class TestEqual(unittest.TestCase):

    def setUp(self):
        self.eq = Equal()
        self.eq.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))
    def test_equal(self):
        result =self.eq.process('x.item=x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$eq" : x.y.item   } }')

        result =self.eq.process('x.item=x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$eq" : x.y.item   } }')


class TestLessThen(unittest.TestCase):

    def setUp(self):
        self.lt = LessThen()
        self.lt.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))
    def test_equal(self):
        result =self.lt.process('x.item<x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$lt" : x.y.item   } }')

        result =self.lt.process('x.item<x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$lt" : x.y.item   } }')


class TestLessThenEqula(unittest.TestCase):

    def setUp(self):
        self.lte = LessThenEqual()
        self.lte.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))
    def test_equal(self):
        result =self.lte.process('x.item<=x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$lte" : x.y.item   } }')

        result =self.lte.process('x.item<=x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$lte" : x.y.item   } }')

class TestGreaterThen(unittest.TestCase):

    def setUp(self):
        self.gt = GreaterThen()
        self.gt.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))
    def test_equal(self):
        result =self.gt.process('x.item>x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$gt" : x.y.item   } }')

        result =self.gt.process('x.item>x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$gt" : x.y.item   } }')


class TestGraterThenEqula(unittest.TestCase):

    def setUp(self):
        self.gte = GreaterThenEqual()
        self.gte.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))
    def test_equal(self):
        result =self.gte.process('x.item>=x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$gte" : x.y.item   } }')

        result =self.gte.process('x.item>=x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$gte" : x.y.item   } }')

class TestNotEqula(unittest.TestCase):

    def setUp(self):
        self.gte = NotEqual()
        self.gte.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))
    def test_equal(self):
        result =self.gte.process('x.item!=x.y.item')
        self.assertEqual(result,'{ "x.item" : { "$ne" : x.y.item   } }')


class TestAnd(unittest.TestCase):

    def setUp(self):
        self.and_process = And()
        self.and_process.set_process_operators(ProcessOperators())
        self.and_process.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))

    def test_equal(self):
        result =self.and_process.process('x.item!=x.y.item $and x.item!=x.y.item')
        self.assertEqual(result,'{ "$and" : [{ "x.item" : { "$ne" : x.y.item    } },{ "x.item" : { "$ne" : x.y.item   } }]   }')


class TestOr(unittest.TestCase):

    def setUp(self):
        self.or_process = Or()
        self.or_process.set_process_operators(ProcessOperators())
        self.or_process.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))

    def test_equal(self):
        result =self.or_process.process('x.item!=x.y.item $or x.item!=x.y.item')
        self.assertEqual(result,'{ "$or" : [{ "x.item" : { "$ne" : x.y.item    } },{ "x.item" : { "$ne" : x.y.item   } }]   }')

class TestNot(unittest.TestCase):

    def setUp(self):
        self.not_process = Not()
        self.not_process.set_process_operators(ProcessOperators())
        self.not_process.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))

    def test_equal(self):
        result =self.not_process.process('$not x.item!=x.y.item')
        self.assertEqual(result,'{ "$not" : { "x.item" : { "$ne" : x.y.item   } } }')


class TestIn(unittest.TestCase):

    def setUp(self):
        self.in_process = In()
        self.in_process.set_process_operators(ProcessOperators())
        self.in_process.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))

    def test_equal(self):
        result =self.in_process.process('x.item $in ["item"]')
        self.assertEqual(result,'{ "x.item " : { "$in" : ["item"] }  }')
        result =self.in_process.process('x.item $in ["item","not item"]')

        self.assertEqual(result,'{ "x.item " : { "$in" : ["item","not item"] }  }')

class TestNotIn(unittest.TestCase):

    def setUp(self):
        self.not_in_process = NotIn()
        self.not_in_process.set_process_operators(ProcessOperators())
        self.not_in_process.set_next(type('Default',(),{'process' : lambda arguemnt: arguemnt}))

    def test_equal(self):
        result =self.not_in_process.process('x.item $nin ["item"]')
        self.assertEqual(result,'{ "x.item " : { "$nin" : ["item"] }  }')
        result =self.not_in_process.process('x.item $nin ["item","not item"]')

        self.assertEqual(result,'{ "x.item " : { "$nin" : ["item","not item"] }  }')
if __name__ == '__main__':
    unittest.main()
