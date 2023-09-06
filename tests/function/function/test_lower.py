from sk_function_solver.function.lower import LowerCase
from sk_function_solver.function.default import MethodDefault
import unittest

class TestLower(unittest.TestCase):

    def setUp(self):
        self.lower = LowerCase()
        self.lower.set_next(MethodDefault())

    def test_max(self):
        value = 'My name is Kibria'
        method = 'lower'
        condition = ''
        result = self.lower.run(value,method,condition)
        self.assertEqual(result,'my name is kibria')


    def test_max_with_condition(self):
        value = 'GKIBRIA'
        method = 'lower'
        condition = '(x)=>x!="kibria"'
        result = self.lower.run(value,method,condition)
        self.assertEqual(result,'gkibria')

if __name__=="__main__":
    unittest.main()