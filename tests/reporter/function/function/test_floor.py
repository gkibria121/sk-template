from sk_report_generator.reporter.function_solver.function.floor import Floor
from sk_report_generator.reporter.function_solver.function.default import MethodDefault
import unittest

class TestFloor(unittest.TestCase):

    def setUp(self):
        self.floor = Floor()
        self.floor.set_next(MethodDefault())

    def test_floor(self):
        value = 2.5
        method = 'floor'
        condition = ''
        result = self.floor.run(value,method,condition)
        self.assertEqual(result,2.0)
    def test_floor_positive_float(self):
        value = 5.7
        method = 'floor'
        condition = ''
        result = self.floor.run(value, method, condition)
        self.assertEqual(result, 5.0)
    def test_floor_negative_float(self):
        value = -3.9
        method = 'floor'
        condition = ''
        result = self.floor.run(value, method, condition)
        self.assertEqual(result, -4.0)
    def test_floor_zero(self):
        value = 0
        method = 'floor'
        condition = ''
        result = self.floor.run(value, method, condition)
        self.assertEqual(result, 0.0)
    def test_floor_large_positive_float(self):
        value = 1000.12345
        method = 'floor'
        condition = ''
        result = self.floor.run(value, method, condition)
        self.assertEqual(result, 1000.0)
    def test_floor_large_negative_float(self):
        value = -9876.54321
        method = 'floor'
        condition = ''
        result = self.floor.run(value, method, condition)
        self.assertEqual(result, -9877.0)
    def test_floor_small_positive_float(self):
        value = 0.00000123
        method = 'floor'
        condition = ''
        result = self.floor.run(value, method, condition)
        self.assertEqual(result, 0.0)
    def test_floor_small_negative_float(self):
        value = -0.00000123
        method = 'floor'
        condition = ''
        result = self.floor.run(value, method, condition)
        self.assertEqual(result, -1.0)

    def test_floor_small_negative_float(self):
        value = 5.2
        method = 'floor'
        significance = '2'
        result = self.floor.run(value, method, significance)
        self.assertEqual(result, 4.0)
        value = 5.9
        method = 'floor'
        significance = '2'
        result = self.floor.run(value, method, significance)
        self.assertEqual(result, 4.0)

        value = 10.2
        method = 'floor'
        significance = '10'
        result = self.floor.run(value, method, significance)
        self.assertEqual(result, 10.0)

    def test_floor_with_condition(self):
        value = 5.2
        method = 'floor'
        significance = '(x)=>x!=5.2,2'
        result = self.floor.run(value, method, significance)
        self.assertEqual(result, 5.2)
        value = 5.9
        method = 'floor'
        significance = '(x)=>x>=5.2,2'
        result = self.floor.run(value, method, significance)
        self.assertEqual(result, 4.0)

        value = 10.2
        method = 'floor'
        significance = '(x)=>x<20,10'
        result = self.floor.run(value, method, significance)
        self.assertEqual(result, 10.0)


if __name__=="__main__":
    unittest.main()