import re
import pyperclip
class RegexFinder:
    def get(self,name):
        return eval(f'self.{name}()')

    def expression(self,level=2):
        floating_point = r'([-+])*\d+(\.\d+)?'
        function_name = r'[a-zA-Z_](\w+)?'
        operators = r'[-+*\/^]+'
        simple_expression = f'({floating_point})(({operators})({floating_point}))*'

        function_arguments = f'{floating_point}(,({floating_point}))*'
        function_calling =f'({function_name})\(({function_arguments})?\)'
        expression_node = f'({simple_expression})|({function_calling})'
        expresssion_with_node = f'({expression_node})(({operators})({expression_node}))*'



        function_arguments_2 = f'({expresssion_with_node})(,({expresssion_with_node}))*'
        function_calling_2 =f'({function_name})\(({function_arguments_2})?\)'
        expression_node_2 = f'({function_calling_2})|({expresssion_with_node})'
        expresssion_with_node_2 = f'({expression_node_2})(({operators})({expression_node_2}))*'



        function_arguments_3 = f'({expresssion_with_node_2})(,({expresssion_with_node_2}))*'
        function_calling_3 =f'({function_name})\(({function_arguments_3})?\)'
        expression_node_3 = f'({function_calling_3})|({expresssion_with_node_2})'
        expresssion_with_node_3 = f'({expression_node_3})(({operators})({expression_node_3}))*'
        # tested until

        function_arguments_4 = f'({expresssion_with_node_3})(,({expresssion_with_node_3}))*'
        function_calling_4 =f'({function_name})\(({function_arguments_4})?\)'
        expression_node_4 = f'({function_calling_4})|({expresssion_with_node_3})'
        expresssion_with_node_4 = f'({expression_node_4})(({operators})({expression_node_4}))*'

        function_arguments_5 = f'({expresssion_with_node_4})(,({expresssion_with_node_4}))*'
        function_calling_5 =f'({function_name})\(({function_arguments_5})?\)'
        expression_node_5 = f'({function_calling_5})|({expresssion_with_node_4})'
        expresssion_with_node_5 = f'({expression_node_5})(({operators})({expression_node_5}))*'



        pyperclip.copy(expresssion_with_node)





##        pattern = f'((?:{expression_elements})|(?:(?:{operators})))+'

        return

    def json_pattern(self):
        json_pattern = r'[\{\}\[\]\]]'

        return json_pattern

regex_finder = RegexFinder()
pattern = regex_finder.get('expression')





##floating_point = r'([-+])*\d+(\.\d+)?'
##
##function_name = r'[a-zA-Z_]\w+'
##operators = r'[-+*\/^]+'
##
##function_arguments = f'(({floating_point})(,({floating_point}))*)'                   #((([-+])*\d+(\.\d+)?)(,(([-+])*\d+(\.\d+)?))*)
##function_calling = f'{function_name}\(({function_arguments})?\)'                      #[a-zA-Z_]\w+\((((([-+])*\d+(\.\d+)?)(,(([-+])*\d+(\.\d+)?))*))?\)
##simple_expression = f'({floating_point})(({operators})({floating_point}))*'          #(([-+])*\d+(\.\d+)?)(([-+*\/^]+)(([-+])*\d+(\.\d+)?))*
##expression_node =f'(({simple_expression})|({function_calling}))'                         #test brackets
##
##expression_with_function = f'({expression_node})(({operators})({expression_node}))*'   #(((([-+])*\d+(\.\d+)?)|([a-zA-Z_]\w+\((((([-+])*\d+(\.\d+)?)(,(([-+])*\d+(\.\d+)?))*))?\))))(([-+*\/^]+)(((([-+])*\d+(\.\d+)?)|([a-zA-Z_]\w+\((((([-+])*\d+(\.\d+)?)(,(([-+])*\d+(\.\d+)?))*))?\)))))*
##
##function_arguments_2 = f'(({expression_node})(,({expression_node}))*)'
##function_calling_2 = f'{function_name}\(({function_arguments_2})?\)'
##expression_node_2 = f'(({simple_expression})|({function_calling_2}))'
##expression_with_function_2 = f'({expression_node_2})(({operators})({expression_node_2}))*'
##
##function_arguments_3 = f'(({expression_node_2})(,({expression_node_2}))*)'
##function_calling_3 = f'{function_name}\(({function_arguments_3})?\)'
##expression_node_3 = f'(({simple_expression})|({function_calling_3}))'
##expression_with_function_3 = f'({expression_node_3})(({operators})({expression_node_3}))*'
##
##function_arguments_4 = f'(({expression_node_3})(,({expression_node_3}))*)'
##function_calling_4 = f'{function_name}\(({function_arguments_4})?\)'
##expression_node_4 = f'(({simple_expression})|({function_calling_4}))'
##expression_with_function_4 = f'({expression_node_4})(({operators})({expression_node_4}))*'