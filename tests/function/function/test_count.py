from sk_function_solver.function.count import Count
from sk_function_solver.function.count import GetCount
from sk_function_solver.function.modules.get_arg import GetArg
from sk_function_solver.function.default import MethodDefault
import unittest

class TestCount(unittest.TestCase):

    def setUp(self):
        self.count = Count()
        self.count.set_next(MethodDefault())

    def test_count(self):
        value = [1,2,3,4]
        method = 'count'
        condition = '1'
        result = self.count.run(value,method,condition)
        self.assertEqual(result,1)

    def testcount_with_duplicates(self):
        value = [1, 2, 3, 2, 4, 3, 1]
        method = 'count'
        condition = '1'
        result = self.count.run(value, method, condition)
        self.assertEqual(result, 2)
    def test_count_empty_list(self):
        value = []
        method = 'count'
        condition = '1'
        result = self.count.run(value, method, condition)
        self.assertEqual(result, 0)
    def test_count_different_method_and_condition(self):
        value = [1, 2, 3, 4]
        method = 'count'
        condition = '2'
        result = self.count.run(value, method, condition)
        self.assertEqual(result, 1)
    def test_count_with_negative_number(self):
        value = [1, 2, -3, 4]
        method = 'count'
        condition = '-3'
        result = self.count.run(value, method, condition)
        self.assertEqual(result, 1)
    def test_count_non_numeric_condition(self):
        value = [1, 2, 3, 4]
        method = 'count'
        condition = 'abc'
        result = self.count.run(value, method, condition)
        self.assertEqual(result,0)
    def test_count_with_float_values(self):
        value = [1.5, 2.7, 3.2, 4.8]
        method = 'count'
        condition = '2'
        result = self.count.run(value, method, condition)
        self.assertEqual(result, 0)

    def test_count_with_str_values(self):
        value = [1.5, '2.7', 3.2, 4.8]
        method = 'count'
        condition = '2.7'
        result = self.count.run(value, method, condition)
        self.assertEqual(result, 1)
class TestGetCount(unittest.TestCase):

    def setUp(self):
        self.get_count = GetCount()
    def test_get_count(self):
        self.assertEqual(self.get_count.run([1, 2, 3, 4],'abc'),0)

    def test_get_count_with_duplicates(self):
        values = [1, 2, 3, 2, 4, 3, 1]
        condition = 2
        result = self.get_count.run(values, condition)
        self.assertEqual(result, 2)
    def test_get_count_empty_list(self):
        values = []
        condition = 1
        result = self.get_count.run(values, condition)
        self.assertEqual(result, 0)
    def test_get_count_all_meeting_condition(self):
        values = [10, 10, 10, 10]
        condition = 10
        result = self.get_count.run(values, condition)
        self.assertEqual(result, 4)
    def test_get_count_with_negative_number(self):
        values = [1, 2, -3, 4]
        condition = -3
        result = self.get_count.run(values, condition)
        self.assertEqual(result, 1)

    def test_get_count_float_condition(self):
        values = [1.5, 2.7, 3.2, 4.8]
        condition = 2.7
        result = self.get_count.run(values, condition)
        self.assertEqual(result, 1)
    def test_get_count_no_matching_condition(self):
        values = [1, 2, 3, 4]
        condition = 5
        result = self.get_count.run(values, condition)
        self.assertEqual(result, 0)

class TestItem(unittest.TestCase):

    def setUp(self):
        self.get_item = GetArg()

    def test_get_item(self):
        self.assertEqual(self.get_item.run('(x)=> 1 in x, 2'),'2')


    def test_significance(self):

        self.assertEqual(self.get_item.run('(x)=>x!=1,2'),'2')
        self.assertEqual(self.get_item.run('(x)=>x!=1,1,2'),'1')

    def test_significance_no_condition(self):

        self.assertEqual(self.get_item.run('2'),'2')

if __name__=='__main__':
    unittest.main()