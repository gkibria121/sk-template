class CreateDeclarationText:
    def run(self,declaration_list):
        declaration_text = ''
        for key,value in declaration_list.items():
            new_text = f'{key} = {value};\n' if type(value)!= str else   f'{key} = "{value}";\n'
            declaration_text+= new_text

        return declaration_text
