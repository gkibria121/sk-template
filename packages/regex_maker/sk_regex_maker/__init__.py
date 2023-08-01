import re
import pyperclip
class RegexMaker:
    def make(self,name):
        return eval(f'self.{name}()')

    def expression(self):
        floating_point = r'([-+])*\d+(\.\d+)?'
        function_name = r'[a-zA-Z_](\w+)?'
        operators = r'[-+*\/^]+'
        simple_expression = f'({floating_point})(({operators})({floating_point}))*'
        simple_expression_with_brackets= f'({simple_expression})|(\({simple_expression}\))'

        function_arguments = f'{floating_point}(,({floating_point}))*'
        function_calling =f'({function_name})\(({function_arguments})?\)'
        expression_node = f'({simple_expression_with_brackets})|({function_calling})'
        expresssion_with_node = f'({expression_node})(({operators})({expression_node}))*'



        function_arguments_2 = f'({expresssion_with_node})(,({expresssion_with_node}))*'
        function_calling_2 =f'({function_name})\(({function_arguments_2})?\)'
        expression_node_with_bracktes_2 = f'({expresssion_with_node})|(\({expresssion_with_node}\))'
        expression_node_2 = f'({function_calling_2})|({expression_node_with_bracktes_2})'
        expresssion_with_node_2 = f'({expression_node_2})(({operators})({expression_node_2}))*'



        function_arguments_3 = f'({expresssion_with_node_2})(,({expresssion_with_node_2}))*'
        function_calling_3 =f'({function_name})\(({function_arguments_3})?\)'
        expression_node_with_bracktes_3 = f'({expresssion_with_node_2})|(\({expresssion_with_node_2}\))'
        expression_node_3 = f'({function_calling_3})|({expression_node_with_bracktes_3})'
        expresssion_with_node_3 = f'({expression_node_3})(({operators})({expression_node_3}))*'
        # tested until

        function_arguments_4 = f'({expresssion_with_node_3})(,({expresssion_with_node_3}))*'
        function_calling_4 =f'({function_name})\(({function_arguments_4})?\)'
        expression_node_with_bracktes_4 = f'({expresssion_with_node_3})|(\({expresssion_with_node_3}\))'

        expression_node_4 = f'({function_calling_4})|({expression_node_with_bracktes_4})'
        expresssion_with_node_4 = f'({expression_node_4})(({operators})({expression_node_4}))*'

        pattern = f"({expresssion_with_node_4})"

        return pattern

    def set_regex_maker(self,regex_maker):
        self.regex_maker = regex_maker

##regex_finder = RegexMaker()
##pattern = regex_finder.make('expression')





