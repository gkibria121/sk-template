import regex as re
from sk_calculator import Calculator
import json


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
                solved_expression[match[1]] = match[2]

            if variable_in_expression:
                temp_expression = match[2]
                for key,value in solved_expression.items():
                    temp_expression = re.sub(re.escape(key)+r'(?=\b)',value,temp_expression)
                variable_in_solved_expression =re.search(r'\$\w+',temp_expression)

                if not variable_in_solved_expression:
                    solved_expression[match[1]]= temp_expression
                else:
                    raise ValueError(variable_in_solved_expression[0]+" Not defined")

        text = ''
        for key,value in solved_expression.items():
            text += f"{key} = {value};"

        return text

    def evaluate_functions(self,variables):
        pattern = r'((cal)(\(([^()]|(?3))*\)))'
        matchs = re.findall(pattern,variables)
        while matchs:
            for match in matchs:
                solved = match[0]
                if match[1]=='cal' or match[1]=='calculate':
                    solved = self.calculator.evaluate(match[2])
                    variables = re.sub(re.escape(match[0]),str(solved),variables)
                variables = re.sub(re.escape(match[0]),str(solved),variables)
            matchs = re.findall(pattern,variables)

        pattern = r'((eval)(\(([^()]|(?3))*\)))'
        matchs = re.findall(pattern,variables)
        while matchs:
            for match in matchs:
                solved = match[0]
                if match[1] =='eval' or match[1] =='evaluate':
                    solved = str(eval(match[2]))
                variables = re.sub(re.escape(match[0]),str(solved),variables)
            matchs = re.findall(pattern,variables)

        return variables

    def process(self, declarations_text):

        declarations = self.remove_comments(declarations_text)
        solve_variables = self.solve_variables(declarations)
        processed_output = self.evaluate_functions(solve_variables)


        return processed_output

variable = '''
$x=cal(1+2);$y=cal(2+1);$var=cal(12+223+(222+2)+sin(90));$var2=cal($x+$y);$xy=cal($var2+$x+$y);$yx=cal($xy+$var2)
'''

data= VariableHandler()
data.set_calculator(Calculator())
print(data.process(variable))
