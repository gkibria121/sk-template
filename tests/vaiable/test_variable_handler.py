from sk_variable_handler.variable_handler import VariableHandler
from sk_variable_handler.variable_handler import SolveFunction
from sk_variable_handler.variable_handler import IsFunction
from sk_variable_handler.variable_handler import IsExpression
from sk_variable_handler.variable_handler import EvaluateValue
from sk_variable_handler.variable_handler import ExpressionSolver
from sk_variable_handler.variable_handler import GenerateText
from sk_variable_handler.variable_handler import GetOriginalType
from sk_variable_handler.variable_handler import IsTable
from sk_variable_handler.variable_handler import SolveFunction
from sk_calculator import Calculator
from sk_regex_maker import RegexMaker
import unittest
from sk_function_solver.function_solver import FunctionSolver
from sk_function_solver.process_function_calling import ProcessFunctionCalling
from sk_function_solver.single_function_solver import SingleFunctionSOlver
from sk_function_solver.get_index_value import GetIndexValue
from sk_function_solver.process_condition import ProcessCondition


class TestGetValues(unittest.TestCase):

    def setUp(self):
        self.variable = VariableHandler()
        self.calculator = Calculator()
        self.variable.set_calculator(self.calculator)
        self.variable.set_calculator(self.calculator)
        self.variable.set_regex_maker(RegexMaker())
        self.variable.set_function_solver(FunctionSolver())
        self.variable.set_get_index(GetIndexValue())
        self.variable.set_process_condition(ProcessCondition())
        self.variable.set_process_function_calling(ProcessFunctionCalling())
        self.variable.set_single_function_solver(SingleFunctionSOlver())
        self.variable.set_next(type('Default',(),{'process' : lambda text: text}))
        self.maxDiff = None
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
$x = $x.name;
'''
        expected_result = '''$x = "John";'''
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
$x = $x.friends[0].name;
'''
        expected_result = "$x = \"Alice\";"
        result = self.variable.process(declarations)
        self.assertEqual(result, expected_result)

from sk_variable_handler.variable_handler import GetOriginalType

class TestGetOriginalType(unittest.TestCase):

    def setUp(self):
        self.get_original_type =GetOriginalType()

    def test_original_type(self):

        result = self.get_original_type.run('12')

        self.assertEqual(result,'12')

        result = self.get_original_type.run('"12"')

        self.assertEqual(result,'"12"')
        result = self.get_original_type.run('[1, 2, 3, 4, 5, 6]')

        self.assertEqual(result,'[1, 2, 3, 4, 5, 6]')


        result = self.get_original_type.run('"[1, 2, 3, 4, 5, 6]"')
        self.assertEqual(result,'"[1, 2, 3, 4, 5, 6]"')


        result = self.get_original_type.run('value1')
        self.assertEqual(result,'"value1"')



        result = self.get_original_type.run('value3')
        self.assertEqual(result,'"value3"')

        result = self.get_original_type.run('$<table:x>select({"x" : "y"})')
        self.assertEqual(result,'"$<table:x>select({"x" : "y"})"')

from sk_variable_handler.variable_handler import GenerateText

class TestGenerateText(unittest.TestCase):
    def setUp(self):
        self.get_original_type = GetOriginalType()
        self.generate_text = GenerateText()
        self.generate_text.set_get_original_type(self.get_original_type)

    def test_generate_text(self):
        result = self.generate_text.run({'$x' : '"y"'})
        self.assertEqual(result,'$x = "y";')

        result = self.generate_text.run({'$x' : '1'})
        self.assertEqual(result,'$x = 1;')

        result = self.generate_text.run({'$x' : '1'})
        self.assertEqual(result,'$x = 1;')

        result = self.generate_text.run({'$x' : '1','$y' : '[1,2,3,4,5]'})
        self.assertEqual(result,'$x = 1;$y = [1,2,3,4,5];')

from sk_variable_handler.variable_handler import TableSolver

class TestTableHandler(unittest.TestCase):
    def setUp(self):
        self.get_original_type = GetOriginalType()
        self.generate_text = GenerateText()
        self.generate_text.set_get_original_type(self.get_original_type)
        self.table_solver = TableSolver()
        self.table_solver.set_generate_text(self.generate_text)
        self.table_solver.set_next(type('Default' ,(),{'process' : lambda text:text}))
    def test_table(self):
        data = {'$x' : 1}
        value = '$<x>select({x : 1})'

        result  = self.table_solver.run(data,value)
        self.assertEqual(result,'$<x>select({x : 1})')




class TestIsFunction(unittest.TestCase):

    def setUp(self):
        self.is_function = IsFunction()

    def test_is_function(self):

        result = self.is_function.run('([1,2,3,4,5]).sum()')
        self.assertEqual(result,True)

        result = self.is_function.run('([1,2,3,4,5])[1].sum()')
        self.assertEqual(result,True)

        result = self.is_function.run('([1,2,3,4,5])[(1)].sum()')
        self.assertEqual(result,True)

        result = self.is_function.run('([1,2,3,4,5])[(1)].sum()')
        self.assertEqual(result,True)

        result = self.is_function.run('([1,2,3,4,5])[("ki")].sum()')
        self.assertEqual(result,True)

        result = self.is_function.run('([1,2,3,4,5])[("ki")].sum((x)=>x).sum((x)=>x)[1].sum((x)=>x)')
        self.assertEqual(result,True)



        result = self.is_function.run('([1,2,3,4,5])[("ki")]')
        self.assertEqual(result,True)

        result = self.is_function.run('([1,2,3,4,5])[("ki")+1-2]')
        self.assertEqual(result,True)


        result = self.is_function.run('([1,2,3,4,5])[("ki")+1-2].max(avg([1,2,3,4]))')
        self.assertEqual(result,True)

class TestIsExpresion(unittest.TestCase):

    def setUp(self):
        self.is_expression  = IsExpression()


    def test_is_expression(self):
        result =self.is_expression.run('@"1+2+3"')
        self.assertEqual(result,True)

        result =self.is_expression.run('"1+2+3"')
        self.assertEqual(result,False)


class TestGenerateText(unittest.TestCase):

    def setUp(self):
        self.generate_text = GenerateText()
        self.generate_text.set_get_original_type(GetOriginalType())


    def test_generate_text(self):

        result = self.generate_text.run({'key' : '"value"'})
        self.assertEqual(result,'key = "value";')


class TestFunctionSolver(unittest.TestCase):

    def setUp(self):
        self.solve_function = SolveFunction()
        self.solve_function.set_function_solver(FunctionSolver())
        self.solve_function.set_get_index(GetIndexValue())
        self.solve_function.set_get_original_type(GetOriginalType())
        self.solve_function.set_process_condition(ProcessCondition())
        self.solve_function.set_process_function_calling(ProcessFunctionCalling())
        self.solve_function.set_single_function_solver(SingleFunctionSOlver())


    def test_function_solver(self):

        result = self.solve_function.run('([1,2,3,4,5])[(2)+1-2]')
        self.assertEqual(result,'2')

        result = self.solve_function.run('([1,2,3,4,5])[[1,2,3][0]]')
        self.assertEqual(result,'2')

        result = self.solve_function.run('([1,"value",3,4,5])[[1,2,3][0]]')
        self.assertEqual(result,'"value"')

        result = self.solve_function.run('([1,2,3,4,5]).sum()')
        self.assertEqual(result,'15')

        result = self.solve_function.run('([1,2,3,4,5]).reverse().sum()')
        self.assertEqual(result,'15')

        result = self.solve_function.run('([1,{"friends" : [1,2,3,4]},3,4,5])[1].friends.reverse().sum()')
        self.assertEqual(result,'10')
        result = self.solve_function.run('([1,{"friends" : [1,2,3,4]},3,4,5])[1].friends.reverse()[1]')
        self.assertEqual(result,'3')


if __name__ == '__main__':
    unittest.main()
