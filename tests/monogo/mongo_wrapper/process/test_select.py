import unittest
from sk_mongo_wrapper.process.select import SelectProcess
from sk_mongo_wrapper.query_process import ArgumentProcess

from sk_mongo_wrapper.process.select.operators.add import Addition
from sk_mongo_wrapper.process.select.operators.sub import Subtraction
from sk_mongo_wrapper.process.select.operators.bracket import Bracket
from sk_mongo_wrapper.process.select.operators.division import Division
from sk_mongo_wrapper.process.select.operators.function import Function
from sk_mongo_wrapper.process.select.operators.multiply import Multiplication
from sk_mongo_wrapper.process.select.operators.reference_process import ReferenceProcess

class TestSelectProcess(unittest.TestCase):

    def setUp(self):
        self.select_process = SelectProcess()
        self.select_process.set_next(type('Default',(),{'process' : lambda name,argument: (name,argument)}))
        self.argument_process =ArgumentProcess()
        self.select_process.set_argument_process(self.argument_process)
        self.argument_process.set_primary_table('x')
    def test_select(self):
        result = self.select_process.process('select','{}')
        self.assertEqual(result,('select','{}'))


        result = self.select_process.process('select',"{'item' : x.item}")
        self.assertEqual(result,('select','{\'item\' :  "$item"}'))

        result = self.select_process.process('select',"{'item' : x.y.item}")
        self.assertEqual(result,('select','{\'item\' :  "$y.item"}'))

        result = self.select_process.process('select',"{'item' : x.y.item }")
        self.assertEqual(result,('select','{\'item\' :  "$y.item" }'))
        self.assertEqual(result, ('select', '{\'item\' :  "$y.item" }'))

        # Test case 2: Selecting a single field
        result = self.select_process.process('select', "{'item': x.item}")
        self.assertEqual(result, ('select','{\'item\':  "$item"}'))

        # Test case 3: Selecting a nested field
        result = self.select_process.process('select', "{'nested_item': x.y.item}")
        self.assertEqual(result, ('select', '{\'nested_item\':  "$y.item"}'))

        # Test case 4: Selecting multiple fields
        result = self.select_process.process('select', "{'field1': x.field1, 'field2': x.field2}")
        self.assertEqual(result, ('select', '{\'field1\':  "$field1", \'field2\':  "$field2"}'))

        result = self.select_process.process('select', "{'field1': x.field1+x.field2, 'field2': x.field2+x.field2}")
        self.assertEqual(result,('select', '{\'field1\': { "$add" : [\'$field1\', \'$field2\'] }, \'field2\': { "$add" : [\'$field2\', \'$field2\'] }}'))

class TestAddProcess(unittest.TestCase):

    def setUp(self):
        self.add_process = Addition()
        self.add_process.set_next(type('Default',(),{'process' : lambda argument: argument}))

    def test_addition(self):
        result = self.add_process.process('1+1')
        self.assertEqual(result, '{ "$add" : [1, 1] }')

        result = self.add_process.process('"x.y"+"x.z"')
        self.assertEqual(result, '{ "$add" : [\'x.y\', \'x.z\'] }')

    def test_multiple_addition(self):
        result = self.add_process.process('1+2+3+4')
        self.assertEqual(result, '{ "$add" : [1, 2, 3, 4] }')

    def test_negative_numbers(self):
        result = self.add_process.process('-5+3')
        self.assertEqual(result, '{ "$add" : [-5, 3] }')

    def test_decimal_numbers(self):
        result = self.add_process.process('2.5+1.75')
        self.assertEqual(result, '{ "$add" : [2.5, 1.75] }')

    def test_mixed_numbers(self):
        result = self.add_process.process('-2.5+3')
        self.assertEqual(result, '{ "$add" : [-2.5, 3] }')

    def test_whitespace(self):
        result = self.add_process.process('  10  +  5  ')
        self.assertEqual(result, '{ "$add" : [10, 5] }')

    def test_empty_string(self):
        result = self.add_process.process('')
        self.assertEqual(result, '')

    def test_invalid_input(self):
        with self.assertRaises(NameError):
            self.add_process.process('1 + a')

class TestSubtractProcess(unittest.TestCase):

    def setUp(self):
        self.sub_process = Subtraction()
        self.sub_process.set_next(type('Default',(),{'process' : lambda argument: argument}))

    def test_addition(self):
        result = self.sub_process.process('1-1')
        self.assertEqual(result, '{ "$subtract" : [1, 1] }')

    def test_negative_result(self):
        result = self.sub_process.process('3-5')
        self.assertEqual(result, '{ "$subtract" : [3, 5] }')

    def test_decimal_numbers(self):
        result = self.sub_process.process('8.5-2.5')
        self.assertEqual(result, '{ "$subtract" : [8.5, 2.5] }')

    def test_mixed_numbers(self):
        result = self.sub_process.process('10-2.5')
        self.assertEqual(result, '{ "$subtract" : [10, 2.5] }')

    def test_whitespace(self):
        result = self.sub_process.process('  15  -  7  ')
        self.assertEqual(result, '{ "$subtract" : [15, 7] }')

    def test_empty_string(self):
        result = self.sub_process.process('')
        self.assertEqual(result, '')

    def test_invalid_input(self):
        with self.assertRaises(NameError):
            self.sub_process.process('5 - b')

class TestMultiplyProcess(unittest.TestCase):

    def setUp(self):
        self.multiplication = Multiplication()
        self.multiplication.set_next(type('Default',(),{'process' : lambda argument: argument}))

    def test_multiply(self):
        result = self.multiplication.process('1*1')
        self.assertEqual(result, '{ "$multiply" : [1, 1] }')

    def test_multiply_negative_numbers(self):
        result = self.multiplication.process('-3*4')
        self.assertEqual(result, '{ "$multiply" : [-3, 4] }')

    def test_multiply_decimal_numbers(self):
        result = self.multiplication.process('2.5*1.5')
        self.assertEqual(result, '{ "$multiply" : [2.5, 1.5] }')

    def test_multiply_mixed_numbers(self):
        result = self.multiplication.process('-2.5*3')
        self.assertEqual(result, '{ "$multiply" : [-2.5, 3] }')

    def test_multiply_zero(self):
        result = self.multiplication.process('5*0')
        self.assertEqual(result, '{ "$multiply" : [5, 0] }')

    def test_multiply_multiple_numbers(self):
        result = self.multiplication.process('2*3*4')
        self.assertEqual(result, '{ "$multiply" : [2, 3, 4] }')

    def test_whitespace(self):
        result = self.multiplication.process('  6  *  7  ')
        self.assertEqual(result, '{ "$multiply" : [6, 7] }')

    def test_empty_string(self):
        result = self.multiplication.process('')
        self.assertEqual(result, '')

    def test_invalid_input(self):
        with self.assertRaises(NameError):
            self.multiplication.process('2 * x')

class TestDivisionProcess(unittest.TestCase):

    def setUp(self):
        self.division = Division()
        self.division.set_next(type('Default',(),{'process' : lambda argument: argument}))

    def test_multiply(self):
        result = self.division.process('1/1')
        self.assertEqual(result, '{ "$divide" : [1, 1] }')
    def test_divide(self):
        result = self.division.process('1/1')
        self.assertEqual(result, '{ "$divide" : [1, 1] }')

    def test_divide_negative_numbers(self):
        result = self.division.process('-10/2')
        self.assertEqual(result, '{ "$divide" : [-10, 2] }')

    def test_divide_decimal_numbers(self):
        result = self.division.process('5.5/2.0')
        self.assertEqual(result, '{ "$divide" : [5.5, 2.0] }')

    def test_divide_mixed_numbers(self):
        result = self.division.process('10/2.5')
        self.assertEqual(result, '{ "$divide" : [10, 2.5] }')

    def test_divide_multiple_numbers(self):
        result = self.division.process('15/3/5')
        self.assertEqual(result, '{ "$divide" : [15, 3, 5] }')

    def test_whitespace(self):
        result = self.division.process('  20  /  4  ')
        self.assertEqual(result, '{ "$divide" : [20, 4] }')

    def test_empty_string(self):
        result = self.division.process('')
        self.assertEqual(result, '')

    def test_invalid_input(self):
        with self.assertRaises(NameError):
            self.division.process('10 / x')

class TestBracketProcess(unittest.TestCase):

    def setUp(self):
        self.bracket = Bracket()
        self.bracket.set_next(type('Default',(),{'process' : lambda argument: argument}))

    def test_multiply(self):
        result = self.bracket.process('(x.y+y.x)')
        self.assertEqual(result, 'x.y+y.x')

    def test_multiply(self):
        result = self.bracket.process('(x.y+y.x)+x.y.z')
        self.assertEqual(result, 'x.y+y.x+x.y.z')

if __name__ == '__main__':
    unittest.main()
