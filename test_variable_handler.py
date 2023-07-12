from sk_variable_handler.variable_handler import VariableHandler
from sk_declaration import DeclarationGenerator
from sk_calculator import Calculator
import unittest
class TestGetValues(unittest.TestCase):
    def setUp(self):
        self.variable =VariableHandler()
        self.calculator = Calculator()
        self.variable.set_calculator(self.calculator)
        self.process = DeclarationGenerator()

    def assert_custom_equal(self,actual, expected):
        if type(actual) != type(expected):
            raise AssertionError(f"Assertion failed: {actual} is not equal to {expected}")

    def test_get_result(self):
        declarations = "$x = 1+2 ; $y = 2 + 1 ; $var = 12 + 223 + ( 222 +2 ) + sin(90) ; $var2 = $x + $y ; $xy = ( $var2 + $x + $y ) ; $yx = $xy + $var2"
        expected_result = {'$x': 3, '$y': 3, '$var': 460, '$var2': 6, '$xy': 12, '$yx': 18}
        result = self.variable.get_result(declarations)
        self.assertEqual(result, expected_result)

    def test_get_result_with_expression(self):
        # Test when there is an expression in the variable declaration
        declarations = "$x = 1 + 2; $y = 2 + 1; $z = $x + $y * 3;"
        expected_result = {'$x': 3, '$y': 3, '$z': 12}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_get_result_with_multiple_expressions(self):
        # Test when there are multiple expressions in the variable declaration
        declarations = "$x = 1 + 2; $y = 2 + 1; $z = $x + $y * 3; $w = $x + $y / 2;"
        expected_result = {'$x': 3, '$y': 3, '$z': 12, '$w': 4.5}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_get_result_with_nested_expressions(self):
        # Test when there are nested expressions in the variable declaration
        declarations = "$x = 1 + 2; $y = 2 + 1; $z = $x + $y * ($x + $y); $w = $x + $y / ($x + $y);"
        expected_result = {'$x': 3, '$y': 3, '$z': 21, '$w': 3.5}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_get_result_with_multiple_variable_assignment(self):
        # Test when there are multiple variable assignments in the expression
        declarations = "$x = 1 + 2; $y = 2 + 1; $z = $x + $y;  $w = $z + $x;"
        expected_result = {'$x': 3, '$y': 3, '$z': 6, '$w': 9}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_get_result_with_complex_expression(self):
        # Test when there is a complex expression in the variable declaration
        declarations = "$x = (1 + 2) * (2 + 1) + sin(90);"
        expected_result = {'$x': 10}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_get_result_with_multiple_complex_expressions(self):
        # Test when there are multiple complex expressions in the variable declaration
        declarations = "$x = (1 + 2) * (2 + 1) + sin(90); $y = (1 + 2) / (2 + 1) + cos(90);"
        expected_result = {'$x': 10, '$y': 1}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)


    def test_get_result_with_no_variables(self):
        # Test when there are no variable declarations
        declarations = "$z = 3 + 4;"
        expected_result = {'$z': 7}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_get_result_with_empty_declaration(self):
        # Test when there is an empty variable declaration
        declarations = "$x = 0; $y = 2 + 1; $z = $x + $y;"
        expected_result = {'$x': 0, '$y': 3, '$z': 3}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)



    def test_get_result_with_nested_complex_expressions(self):
        # Test when there are nested complex expressions in the variable declaration
        declarations = "$x = (1 + 2) * ((2 + 1) + sin(90));"
        expected_result = {'$x': 12}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        # Test when there is whitespace in the variable declaration
        declarations = " $x = 1 + 2 ; $y = 2 + 1 ; $z = $x + $y ; "
        expected_result = {'$x': 3, '$y': 3, '$z': 6}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        # Test when there are multiple complex expressions in the variable declaration
        declarations = "$x = (1 + 2) * (2 + 1) + sin(90); $y = (1 + 2) / (2 + 1) + cos(90);"
        expected_result = {'$x': 10, '$y': 1}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        # Test when there is a complex expression in the variable declaration
        declarations = "$x = (1 + 2) * (2 + 1) + sin(90);"
        expected_result = {'$x': 10}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_get_result_with_multiple_variable_in_complex_expression(self):
        # Test when there are multiple variables in the complex expression
        declarations = "$x = 1 + 2; $y = 2 + 1; $z = ($x + $y) * ($x + $y) + sin(90);"
        expected_result = {'$x': 3, '$y': 3, '$z': 37}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        # Test when there is a variable in the complex expression
        declarations = "$x = 1 + 2; $y = 2 + 1; $z = ($x + $y) * (2 + 1) + sin(90);"
        expected_result = {'$x': 3, '$y': 3, '$z': 19}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    # Test when there is a variable assignment in the expression
    def test_get_result_with_variable_assignment(self):
        declarations = "$x = 1 + 2; $y = 2 + 1; $z = $x + $y; "
        expected_result = {'$x': 3, '$y': 3, '$z': 6}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_get_result_with_list_object(self):
        # Test when there is a list object in the variable declaration
        declarations = "$list = [1,2, 3, 4];"
        expected_result = {'$list': [1,2,3,4]}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)



    def test_get_result_with_list_and_dictionary(self):
        # Test when there are both list and dictionary objects in the variable declaration
        declarations = "$list = [1, 2, 3, 4]; $dict = {'key1': 'value1', 'key2': 'value2'};"
        expected_result = {'$list': [1,2,3,4], '$dict': {'key1': 'value1', 'key2': 'value2'}}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        # Test when there is a dictionary in the variable declaration
        declarations = "$dict = {'key1': 'value1', 'key2': 'value2'};"
        expected_result = {'$dict': {'key1': 'value1', 'key2': 'value2'}}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

    def test_recursive_variable(self):
        declarations =  "$x = 1 + 2; $y = 2 + 1; $z = $x + $y;  $z = $z + $x; $z = $z*2; $z = $z +1;"
        expected_result = {'$x': 3, '$y': 3, '$z': 19}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        declarations =  "$x =0; $x = $x+2; $x = 1+2"
        expected_result = {'$x': 3}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        declarations =  "$x = 0;$x = $x+2; $x = $x+2"
        expected_result = {'$x' : 4}
        result = self.variable.get_result(self.process.process(declarations))

        self.assertEqual(result, expected_result)
        declarations =  "$x= 0;$x = $x+2; $x = $x+2 ; $x = 0;"
        expected_result = {'$x' : 0}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        declarations =  "$x=0;$x = $x+2; $x = $x+2 ; $x =1;"
        expected_result = {'$x' : 1}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        declarations =  "$x = {'x':2};"
        expected_result ={'$x': {'x':2}}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)



    def test_python_variable(self):

        # Test when there are both list and dictionary objects in the variable declaration
        declarations = "list = [1, 2, 3, 4] \ndict = {'key1': 'value1', 'key2': 'value2'};"
        expected_result = {'$list': [1,2,3,4], '$dict': {'key1': 'value1', 'key2': 'value2'}}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)
        declarations =  "x = 1 + 2\ny = 2 + 1\nz = x + y\nz = z + x\nz = z*2\nz = z +1;"
        expected_result = {'$x': 3, '$y': 3, '$z': 19}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        declarations =  "x =0\nx = x+2\nx = 1+2"
        expected_result = {'$x': 3}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        declarations =  "x = 0\nx = x+2\nx = x+2"
        expected_result = {'$x' : 4}
        result = self.variable.get_result(self.process.process(declarations))

        self.assertEqual(result, expected_result)
        declarations =  "x= 0\nx = x+2\nx = x+2 \nx = 0;"
        expected_result = {'$x' : 0}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        declarations =  "x=0\nx = x+2\nx = x+2 \nx =1;"
        expected_result = {'$x' : 1}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)

        declarations =  "x = {'x':2};"
        expected_result ={'$x': {'x':2}}
        result = self.variable.get_result(self.process.process(declarations))
        self.assertEqual(result, expected_result)


    def test_random_functions(self):

        declarations =  "x =random_list()"
        expected_result =list()
        result = self.variable.get_result(self.process.process(declarations))
        self.assert_custom_equal(result['$x'], expected_result)

        declarations =  "x =random_nested()"
        expected_result =list()
        result = self.variable.get_result(self.process.process(declarations))
        self.assert_custom_equal(result['$x'], expected_result)

        declarations =  "x =random_object()"
        expected_result =dict()
        result = self.variable.get_result(self.process.process(declarations))
        self.assert_custom_equal(result['$x'], expected_result)

        declarations =  "x =random_nested_object()"
        expected_result =dict()
        result = self.variable.get_result(self.process.process(declarations))
        self.assert_custom_equal(result['$x'], expected_result)

        declarations =  "x =random_word()"
        expected_result =str()
        result = self.variable.get_result(self.process.process(declarations))
        self.assert_custom_equal(result['$x'], expected_result)

        declarations =  "x =random_digit()"
        expected_result =int()
        result = self.variable.get_result(self.process.process(declarations))
        self.assert_custom_equal(result['$x'], expected_result)

        declarations =  "x =random_json()"
        result = self.variable.get_result(self.process.process(declarations))

        if type(result) == list or type(result) == dict:
            pass
        else:
            raise AssertionError('Not a valid json')

        declarations =  "x =random_data()"
        expected_result =int()
        result = self.variable.get_result(self.process.process(declarations))
        if result =='':
            raise AssertionError('Empty data')

if __name__ == '__main__':
    unittest.main()