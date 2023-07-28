from sk_random_variable import RandomVariableGenerator

import unittest



class TestRandomVariableGenerator(unittest.TestCase):
    def setUp(self):
        self.declaration = RandomVariableGenerator()


    def test_get_result(self):
        declarations = "$x=random_json();"
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)


        declarations = '$x = random_data();'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)

        declarations = '$y = random_word();'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)

        declarations = '$z = random_list();'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)

        declarations = '$a = random_nested_list();'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)

        declarations = '$b = random_nested_object();'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)

        declarations = '$k = random_list(0,1,5);'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)

        declarations = '$q = random_list(start =1,end = 10, length = 3);'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)

        declarations = '$w = random_nested_list(dimensions = [2,3,3]);'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)
        declarations = "$r = random_nested_object(keys = ['x','y','z','a','b','c'],values = [2,3,4,5,6]);"
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)
        declarations = '$x =1+ random_digit();'
        result = self.declaration.process(declarations)
        self.assertEqual(type(result),str)

if __name__ == '__main__':
    unittest.main()
