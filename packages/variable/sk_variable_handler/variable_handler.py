import regex as re
import json
from sk_calculator import Calculator
class VariableHandler:

    def __init__(self):
        self.calculator = None

    def set_calculator(self, calculator):

        self.calculator = calculator

    def remove_comments(self, declarations):
        single_line_comment = r'\#.*+($)?'
        declarations = re.sub(single_line_comment, '', declarations)
        multiline_comment = r'\/\*[\s\S]*?\*\/'
        declarations = re.sub(multiline_comment, '', declarations)
        extra_space = r'\n\s*'
        declarations = re.sub(extra_space, '', declarations)
        declarations = declarations.strip()
        return declarations


    def solve_variables(self,declaraions):
        solved_expression = {}

        pattern = r'((\$\w+)\s*=\s*([^;]+);)'

        matches = re.findall(pattern,declaraions)
        for match in matches:
            variable_in_expression =re.search(r'\$\w+',match[2])
            if  not variable_in_expression:
                solved_expression[match[1]] =self.eval_value(match[2])

            if variable_in_expression:
                temp_expression = match[2]
                for key,value in solved_expression.items():
                    temp_expression = re.sub(re.escape(key)+r'(?=\b)',value,temp_expression)
                variable_in_solved_expression =re.search(r'\$\w+',temp_expression)

                if not variable_in_solved_expression:
                    solved_expression[match[1]]=self.eval_value(temp_expression)
                else:
                    raise NameError(variable_in_solved_expression[0]+" Not defined")

        text = ''
        for key,value in solved_expression.items():
            text += f"{key} = {value};"

        return text


    def eval_value(self,value):
        is_expression = self.is_expression(value)
        if is_expression:
            value = self.solve_expression(value)

        if self.is_object(value):
            value = str(eval(value))


        return value

    def process(self, declarations_text):

        declarations = self.remove_comments(declarations_text)
        solve_variables = self.solve_variables(declarations)
        return solve_variables

    def is_expression(self,value):
        pattern = r'\@((\"([^\"]+)\")|(\'([^\']+)\'))'
        expression = re.search(pattern,value)
        if expression:
            return True

        return False

    def is_object(self,value):

        pattern = r'[\{\}\[\]\]]'
        if re.search(pattern,value):
            return True

        return False




    def solve_expression(self,expression):

        pattern = r'\@((\"([^\"]+)\")|(\'([^\']+)\'))'

        expression = re.sub(pattern,lambda match: str(self.calculator.evaluate(match[3])) if match[5] ==None else str(self.calculator.evaluate(match[5])),expression)
        return expression


    def set_regex_maker(self,regex_maker):
        self.regex_maker = regex_maker

variable = "$x = [5 , @'5+10'];$y = $x+[3];$z =$y+[2, @'1+2^3'];"

data= VariableHandler()
data.set_calculator(Calculator())
print(data.process(variable))
