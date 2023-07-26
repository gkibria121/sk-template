from sk_report_generator.reporter.function_solver.function.round import Round
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestSet(unittest.TestCase):

    def setUp(self):
        self.round = Round()
        self.round.set_next(MethodDefault())

    def test_round(self):
        value = 10.1111111111111
        method = 'round'
        condition = '9'
        result = self.round.run(value,method,condition)
        self.assertEqual(result,10.111111111)

        value = 10.12345678

        condition = '3'
        result = self.round.run(value,method,condition)
        self.assertEqual(result,10.123)

        condition = '6'
        result = self.round.run(value,method,condition)
        self.assertEqual(result,10.123457)

    def test_round_with_condition(self):

        value = 10.12345678
        method = 'round'
        condition = '(x)=>x>10 ,6'
        result = self.round.run(value,method,condition)
        self.assertEqual(result,10.123457)

        value = 10.12345678
        method = 'round'
        condition = '(x)=>x==10 ,6'
        result = self.round.run(value,method,condition)
        self.assertEqual(result,10.12345678)
if __name__=='__main__':
    unittest.main()