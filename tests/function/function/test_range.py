import unittest
from sk_function_solver.function.range import Range
from sk_function_solver.function.range import CustomRange
from sk_function_solver.function.range import DefaultRange
from sk_function_solver.function.range import Default
from sk_function_solver.function.default import MethodDefault


class TestRange(unittest.TestCase):

    def setUp(self):
        self.range = Range()
        self.range.set_next(MethodDefault())

    def test_range(self):
        value = [1,2,3]
        method = 'range'
        condition = '1'
        result =self.range.run(value,method,condition)
        self.assertEqual(result,[2,3])

        condition = '1,3'
        result =self.range.run(value,method,condition)
        self.assertEqual(result,[2,3])

        condition = '1,2'
        result =self.range.run(value,method,condition)
        self.assertEqual(result,[2])

        value = [i for i in range(100)]
        condition = '0,100,5'
        result =self.range.run(value,method,condition)
        self.assertEqual(result,[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

        condition = '0,-1,5'
        result =self.range.run(value,method,condition)
        self.assertEqual(result,[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

class TestDefaultRange(unittest.TestCase):

    def setUp(self):
        self.range = DefaultRange()
        self.range.set_next(Default())

    def test_range(self):
        value = [1,2,3]

        condition = ['1']
        result =self.range.run(value,condition)
        self.assertEqual(result,[2,3])

        condition = ['1','3']
        result =self.range.run(value,condition)
        self.assertEqual(result,[2,3])

        condition = ['1','2']
        result =self.range.run(value,condition)
        self.assertEqual(result,[2])

        value = [i for i in range(100)]
        condition = ['0','100','5']
        result =self.range.run(value,condition)
        self.assertEqual(result,[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])

        condition = ['0','-1','5']
        result =self.range.run(value,condition)
        self.assertEqual(result,[0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, 85, 90, 95])



class TestCustomRange(unittest.TestCase):

    def setUp(self):
        self.range = CustomRange()
        self.range.set_next(Default())

    def test_range(self):
        value = "hi there how are you"

        condition = ['1','w']
        result =self.range.run(value,condition)
        self.assertEqual(result,'there how are you')

        condition = ['1','3','w']
        result =self.range.run(value,condition)
        self.assertEqual(result,'there how')

        condition = ['1','2','w']
        result =self.range.run(value,condition)
        self.assertEqual(result,'there')

        condition = ['3','1','-1','w']
        result =self.range.run(value,condition)
        self.assertEqual(result,'are how')






if __name__=='__main__':
    unittest.main()