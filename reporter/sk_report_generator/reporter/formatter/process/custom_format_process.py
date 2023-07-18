import regex as re
class CustomFormatProcess:

    def __init__(self):
        self.get_condition = GetCondition()



    def run(self,value, format_spec, format_class_list):

        matches = re.split(',', format_spec)
        condition = re.search(r'c(\(((?>[^()]+|(?1))*)\))', format_spec)

        format_spec_list = matches
        format_specs = {}
        if condition:

            condition =self.get_condition.run(value,condition[2])

            format_spec_list = matches[1:]
        else:
            condition = True
        for key in format_spec_list:
            format_specs.update(format_class_list[key])

        return condition,format_specs

class GetCondition:
    def run(self,value,condition):
        pattern = r'\((\w+)\)\=\>(.*)'

        match = re.search(pattern,condition)

        try:
            exec(f'{match[1]} = {value}')
        except NameError:
            exec(f'{match[1]} = "{value}"')


        if eval(f'{match[2]}'):
            return True

        return False
