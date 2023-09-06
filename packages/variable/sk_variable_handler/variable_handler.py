import regex as re
import json



class VariableHandler:

    def __init__(self):
        self.calculator = None
        self.function_solver = None
        self.successor = None
        self.data = None
        self.process_function_calling = None
        self.single_function_solver = None
        self.get_index = None
        self.process_condition = None
        self.function_solver = None





    def set_process_function_calling(self,function):
        self.process_function_calling = function

    def set_single_function_solver(self,solver):
        self.single_function_solver = solver

    def set_get_index(self,index):
        self.get_index = index
    def set_function_solver(self,solver):
        self.function_solver = solver
    def set_process_condition(self,condition):
        self.process_condition = condition






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
        self.single_function_solver.set_get_index_value(self.get_index)
        self.single_function_solver.set_process_condition(self.process_condition)

        self.function_solver.set_process_function_calling(self.process_function_calling)
        self.function_solver.set_single_obj_solver(self.single_function_solver)

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
                    temp_expression = re.sub(re.escape(key)+r'(?=\b)',f"({value})",temp_expression)
                variable_in_solved_expression =re.search(r'\$\w+',temp_expression)

                if not variable_in_solved_expression:
                    solved_expression[match[1]]=self.eval_value(temp_expression)
                else:
                    raise NameError(variable_in_solved_expression[0]+" Not defined")

        text = ''
        for key,value in solved_expression.items():

            value = self.get_original_type(value)
            text += f"{key} = {value};"


        return text

    def get_original_type(self,value):
        flag = True
        try:
            value = eval(value) if type(value)==str else value
            flag = True
        except:
            flag = False

        if type(value)==str and flag:
            value = f'"{value}"'
        return value
    def eval_value(self,value):
        is_function= self.is_function(value)
        if is_function:
            value = self.solve_function(value)

        is_expression = self.is_expression(value)
        if is_expression:
            value = self.solve_expression(value)
        return value

    def solve_function(self,function_calling):
        value_of_function = function_calling
        pattern = r'((\(([^()]|(?2))*\))((\[\d+\])?((\.\w+(?2)?)|(\[\d+\]))+))'
        matches = re.findall(pattern,value_of_function)
        for match in matches:
            self.function_solver.set_data({'$function_name' : eval(match[1])})
            evaluated_value =self.function_solver.solve('$function_name'+match[3])
            try:
                evaluated_value = eval(evaluated_value)
                evaluated_value = f"{evaluated_value}"
            except:
                evaluated_value = f'"{evaluated_value}"'
            value_of_function = re.sub(re.escape(match[0]),evaluated_value,value_of_function)
        return value_of_function




    def is_function(self,value):
        pattern  = r'((\(([^()]|(?2))*\))((\[\d+\])?((\.\w+(?2)?)|(\[\d+\]))+))'
        return re.search(pattern,value)

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

    def solve_expression(self,expression):

        pattern = r'\@((\"([^\"]+)\")|(\'([^\']+)\'))'

        expression = re.sub(pattern,lambda match: str(self.calculator.evaluate(match[3])) if match[5] ==None else str(self.calculator.evaluate(match[5])),expression)
        return expression


    def set_regex_maker(self,regex_maker):
        self.regex_maker = regex_maker

    def set_function_solver(self,function_solver):
        self.function_solver  = function_solver



##variable = "$x=@'1+2';$y=@'2+1';$var=@'12+223+(222+2)+sin(90)';$var2= $x+$y;$xy=($var2+$x+$y);$yx=$xy+$var2;"
##
##data= VariableHandler()
##data.set_calculator(Calculator())
##print(data.process(variable))
