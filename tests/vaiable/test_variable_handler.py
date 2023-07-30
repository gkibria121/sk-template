from sk_variable_handler.variable_handler import VariableHandler
from sk_calculator import Calculator
import unittest


class TestGetValues(unittest.TestCase):

    def setUp(self):
        self.variable = VariableHandler()
        self.calculator = Calculator()
        self.variable.set_calculator(self.calculator)

    def test_get_result(self):
        declarations = "$x=1+2;$y=2+1;$var=12+223+(222+2)+sin(90);$var2=$x+$y;$xy=($var2+$x+$y);$yx=$xy+$var2;"
        expected_result = "$x = 1+2;$y = 2+1;$var = 12+223+(222+2)+sin(90);$var2 = 6;$xy = 12;$yx = 18;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

        declarations = "$x=cal(1+2);$y=cal(2+1);$var=cal(12+223+(222+2)+sin(90));$var2=cal($x+$y);$xy=cal($var2+$x+$y);$yx=cal($xy+$var2)"
        expected_result = "$x = 3;$y = 3;$var = 460;$var2 = 6;$xy = 12;"
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

    def test_get_invalid_variable(self):
        # Test getting an invalid variable (a variable that is not defined)
        declarations = "$x = 5;$y = $z+1;"
        # Since $z is not defined, it should raise an error
        with self.assertRaises(NameError):
            self.variable.process(declarations)

    def test_get_nested_variables(self):
        # Test getting the value of a nested variable
        declarations = "$x = 5;$y = $x+3;$z = $y*2;"
        expected_result = "$x = 5;$y = 8;$z = 16;"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)


if __name__ == '__main__':
    unittest.main()
