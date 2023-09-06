from sk_variable_handler.variable_handler import VariableHandler
from sk_calculator import Calculator
from sk_regex_maker import RegexMaker
import unittest


class TestGetValues(unittest.TestCase):

    def setUp(self):
        self.variable = VariableHandler()
        self.calculator = Calculator()
        self.variable.set_calculator(self.calculator)
        self.variable.set_calculator(self.calculator)
        self.variable.set_regex_maker(RegexMaker())


    def test_get_result(self):
        declarations = "$x=@'1+2';$y=@'2+1';$var=@'12+223+(222+2)+sin(90)';$var2= $x+$y;$xy=($var2+$x+$y);$yx=$xy+$var2;"
        expected_result = "$x = 3;$y = 3;$var = 460;$var2 = 6;$xy = 12;$yx = 18;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)
    def test_get_result_2(self):
        declarations = "$x=@'1+2';$y=@'2+1';$var=@'12+223+(222+2)+sin(90)';$var2= \"$x+$y\";"
        expected_result = "$x = 3;$y = 3;$var = 460;$var2 = \"(3)+(3)\";"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)
    def test_get_single_variable(self):
        # Test getting the value of a single variable
        declarations = "$x = 10;"
        expected_result = "$x = 10;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

    def test_get_multiple_variables(self):
        # Test getting the values of multiple variables
        declarations = "$x = 1;$y = 2;$z = 3;"
        expected_result = "$x = 1;$y = 2;$z = 3;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)


    def test_get_nested_variables(self):
        # Test getting the value of a nested variable
        declarations = "$x = 5;$y = @'$x+3';$z = @'$y*2';"
        expected_result = "$x = 5;$y = 8;$z = 16;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

    def test_get_list_variables(self):
        # Test getting the value of a nested variable
        declarations = "$x = [5];$y = $x+[3];$z =$y+[2];"
        expected_result = "$x = [5];$y = [5, 3];$z = [5, 3, 2];"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

    def test_expression_in_list(self):
        # Test getting the value of a nested variable
        declarations = "$x = [5 ,@\"5+10\"];$y = $x+[3];$z =$y+[2];"
        expected_result = "$x = [5, 15];$y = [5, 15, 3];$z = [5, 15, 3, 2];"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)
    def test_nested_expressions(self):
        declarations = "$x = [5 , @\"5+10\"];$y = @'$x+[3]';$z =$y+[2, @'1+2^3'];"
        expected_result = "$x = [5, 15];$y = [5, 15, 3];$z = [5, 15, 3, 2, 9];"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)
    def test_mathematical_expressions(self):
        declarations = "$x = @'5+3*2';$y = @'sin(45)';$z = @'cos($x) + tan($y)';"
        expected_result = "$x = 11;$y = 0.707106781;$z = 0.9939691509999999;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)
    def test_complex_nested_variables(self):
        declarations = "$x = 10;$y = @'$x + 5';$z = @'$x * $y - ($x + $y)';"
        expected_result = "$x = 10;$y = 15;$z = 125;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

    def test_mixed_data_list(self):
        declarations = "$x = [1, 'hello', 3.14];$y = $x + [True, None];"
        expected_result = "$x = [1, 'hello', 3.14];$y = [1, 'hello', 3.14, True, None];"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

    def test_loop_constructs(self):
        declarations = "$x = 1;$sum = 0;"
        expected_result = "$x = 1;$sum = 0;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

    def test_recursive_variable(self):
        # Test a recursive variable definition
        declarations = "$x = 5;$y = 2 * $x + 1;$x = $x + $y;"
        expected_result = "$x = 16;$y = 11;"  # $x will be evaluated as 18 in the second line
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

    def test_recursive_variable(self):
        # Test a recursive variable definition
        declarations = "$x = @'5+1';$y = @'2 * $x + 1';$x = @'$x + $y';"
        expected_result = "$x = 19;$y = 13;"  # $x will be evaluated as 18 in the second line
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

    def test_indirect_recursive_variable(self):
        # Test indirect recursive variable definitions
        declarations = "$x = $y;$y = $x + 1;"
        expected_result = "$x = $y;$y = $x + 1;"  # $x and $y will form an infinite loop of 1

        with self.assertRaises(NameError):
            self.variable.process(declarations)



    def test_empty_expression(self):
        # Test an empty expression
        declarations = ""
        result = self.variable.process(declarations)
        self.assertEqual(result, "")




    def test_empty_expression_not(self):
        # Test an empty expression
        declarations = "$x= '2';"
        result = self.variable.process(declarations)
        self.assertEqual(result, "$x = \"2\";")



    def test_get_result(self):
        declarations = "$x=@'1+2';$y=@'2+1';$var=@'12+223+(222+2)+sin(90)';$var2= $x+$y;$xy=@'($var2+$x+$y)';$yx=$xy+$var2;"
        expected_result = "$x = 3;$y = 3;$var = 460;$var2 = 6;$xy = 12;$yx = 18;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)


    def test_dot_convention(self):
        declarations = '''$x={
    'name': 'John',
    'age': 30,
    'hobbies': ['Reading', 'Hiking', 'Gaming'],
    'address': {
        'street': '123 Main St',
        'city': 'Cityville',
        'zipCode': '12345'
    },
    'friends': [
        {'name': 'Alice', 'age': 28},
        {'name': 'Bob', 'age': 32},
        {'name': 'Eve', 'age': 29}
    ]
};
$y = $x.name;
'''
        expected_result = "$x = {'name': 'John', 'age': 30, 'hobbies': ['Reading', 'Hiking', 'Gaming'], 'address': {'street': '123 Main St', 'city': 'Cityville', 'zipCode': '12345'}, 'friends': [{'name': 'Alice', 'age': 28}, {'name': 'Bob', 'age': 32}, {'name': 'Eve', 'age': 29}]};$y = \"John\";"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

        declarations = '''$x={
    'name': 'John',
    'age': 30,
    'hobbies': ['Reading', 'Hiking', 'Gaming'],
    'address': {
        'street': '123 Main St',
        'city': 'Cityville',
        'zipCode': '12345'
    },
    'friends': [
        {'name': 'Alice', 'age': 28},
        {'name': 'Bob', 'age': 32},
        {'name': 'Eve', 'age': 29}
    ]
};
$y = $x.friends[0].name;
'''
        expected_result = "$x = {'name': 'John', 'age': 30, 'hobbies': ['Reading', 'Hiking', 'Gaming'], 'address': {'street': '123 Main St', 'city': 'Cityville', 'zipCode': '12345'}, 'friends': [{'name': 'Alice', 'age': 28}, {'name': 'Bob', 'age': 32}, {'name': 'Eve', 'age': 29}]};$y = \"Alice\";"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

if __name__ == '__main__':
    unittest.main()
