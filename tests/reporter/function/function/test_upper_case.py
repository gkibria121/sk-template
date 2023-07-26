from sk_report_generator.reporter.function_solver.function.upper_case import UpperCase
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class Testupper(unittest.TestCase):

    def setUp(self):
        self.upper = UpperCase()
        self.upper.set_next(MethodDefault())

    def test_max(self):
        value = 'My name is Kibria'
        method = 'upper'
        condition = ''
        result = self.upper.run(value,method,condition)
        self.assertEqual(result,'MY NAME IS KIBRIA')


    def test_max_with_condition(self):
        value = 'gkibria'
        method = 'upper'
        condition = '(x)=>x!="kibria"'
        result = self.upper.run(value,method,condition)
        self.assertEqual(result,'GKIBRIA')

if __name__=="__main__":
    unittest.main()