from sk_table_hanlder.process.get_variable_tokens import GetVariableTokens
import unittest


class TestCreateDeclarationText(unittest.TestCase):

    def setUp(self):

        self.get_variable_tokens = GetVariableTokens()

    def test_text(self):

        variables  =''
        result = self.get_variable_tokens.run(variables)
        self.assertEqual(result,[])


        variables  =''.join([f'$key{i} = value{i};\n' for i in range(11)])
        result = self.get_variable_tokens.run(variables)
        self.assertEqual(result,[(f'$key{i}',f'value{i}') for i in range(11)])


if __name__=='__main__':
    unittest.main()