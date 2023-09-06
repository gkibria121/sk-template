from sk_function_solver.function.slice import Slice
from sk_function_solver.function.default import MethodDefault
import unittest

class TestSlice(unittest.TestCase):

    def setUp(self):
        self.slice = Slice()
        self.slice.set_next(MethodDefault())

    def test_slice(self):
        value = [1,2,3,4]
        method = 'slice'
        condition = '1'
        result = self.slice.run(value,method,condition)
        self.assertEqual(result,[2, 3, 4])

        value = [1,2,3,4]
        method = 'slice'
        condition = '4'
        result = self.slice.run(value,method,condition)
        self.assertEqual(result,[])

        value = [1,2,3,4]
        method = 'slice'
        condition = '1,3'
        result = self.slice.run(value,method,condition)
        self.assertEqual(result,[2, 3])

        value = [1,2,3,4]
        method = 'slice'
        condition = '-1'
        result = self.slice.run(value,method,condition)
        self.assertEqual(result,[4, 3, 2, 1])

if __name__=='__main__':
    unittest.main()