class CreateDeclarationText:
    def run(self,declaration_list):
        declaration_text = ''
        for key,value in declaration_list.items():
            declaration_text+= f'{key} = {value};\n'

        return declaration_text
