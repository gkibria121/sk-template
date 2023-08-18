from sk_table_hanlder.process.create_declaration_list import CreateDeclarationText
import unittest


class TestCreateDeclarationText(unittest.TestCase):

    def setUp(self):

        self.create_declaration_text = CreateDeclarationText()

    def test_text(self):

        lis = {f"key{i}" : f"value{i}" for i in range(11)}
        result = self.create_declaration_text.run(lis)
        self.maxDiff = None
        self.assertEqual(result,''.join([f'key{i} = value{i};\n' for i in range(11)]))




if __name__=='__main__':
    unittest.main()