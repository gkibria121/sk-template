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
        self.solve_variables = SolveVariables()
        self.generate_text =GenerateText()
        self.get_original_type = GetOriginalType()
        self.generate_text.set_get_original_type(self.get_original_type)

        self.eval_value = EvaluateValue()
        self.is_expression = IsExpression()
        self.is_function = IsFunction()
        self.is_table = IsTable()
        self.solve_function = SolveFunction()
        self.solve_function.set_get_original_type(self.get_original_type)

        self.solve_expression = ExpressionSolver()
        self.solve_table =TableSolver()

        self.solve_table.set_generate_text(self.generate_text)

        self.eval_value.set_is_expression(self.is_expression)
        self.eval_value.set_is_function(self.is_function)
        self.eval_value.set_is_table(self.is_table)
        self.eval_value.set_solve_expression(self.solve_expression)
        self.eval_value.set_solve_table(self.solve_table)
        self.eval_value.set_solve_function(self.solve_function)

        self.solve_variables.set_eval_value(self.eval_value)



    def process(self, declarations_text):

        solve_variables = self.solve_variables.run(declarations_text)

        text = self.generate_text.run(solve_variables)
        return self.go_next.process(text)




    def set_regex_maker(self,regex_maker):
        self.regex_maker = regex_maker

    def set_function_solver(self,function_solver):
        self.function_solver  = function_solver
        self.solve_function.set_function_solver(self.function_solver)


    def set_next(self,go_next):
        self.go_next = go_next
        self.solve_table.set_next(go_next)


    def set_process_function_calling(self,function):
        self.process_function_calling = function
        self.solve_function.set_process_function_calling(self.process_function_calling)

    def set_single_function_solver(self,solver):
        self.single_function_solver = solver
        self.solve_function.set_single_function_solver(self.single_function_solver)


    def set_get_index(self,index):
        self.get_index = index
        self.solve_function.set_get_index(self.get_index)

    def set_function_solver(self,solver):
        self.function_solver = solver
        self.solve_function.set_function_solver(self.function_solver)
    def set_process_condition(self,condition):
        self.process_condition = condition
        self.solve_function.set_process_condition(self.process_condition)

    def set_calculator(self, calculator):

        self.calculator = calculator
        self.solve_expression.set_calculator(self.calculator)



class SolveVariables:
    def __init__(self):
        self.single_function_solver = None
        self.eval_value = None
        self.function_solver = None
        self.get_index = None
        self.process_condition = None
        self.process_function_calling = None


    def run(self,declaraions):
        solved_expression = {}

        pattern = r'((\$\w+)\s*=\s*([^;]+);)'

        matches = re.findall(pattern,declaraions)
        for match in matches:
            variable_in_expression = re.search(r'\$\w+',match[2])
            if  not variable_in_expression:
                solved_expression[match[1]] =self.eval_value.run(solved_expression,match[2])

            if variable_in_expression:
                temp_expression = match[2]
                for key,value in solved_expression.items():
                    temp_expression = re.sub(re.escape(key)+r'(?=\b)',f"({value})",temp_expression)

                variable_in_solved_expression = re.search(r'\$\w+',temp_expression)

                if not variable_in_solved_expression:
                    solved_expression[match[1]]=self.eval_value.run(solved_expression,temp_expression)
                else:
                    raise NameError(variable_in_solved_expression[0]+" Not defined")
        return solved_expression



    def set_eval_value(self,value):
        self.eval_value = value

class EvaluateValue:
    def set_function_solver(self,function_solver):
        self.function_solver  = function_solver
        self.solve_function.set_function_solver(function_solver)

    def run(self,data,value):
        is_function= self.is_function.run(value)
        if is_function:
            value = self.solve_function.run(value)

        is_expression = self.is_expression.run(value)
        if is_expression:

            value = self.solve_expression.run(value)
        is_table = self.is_table.run(value)
        if is_table:
            value = self.table_solver.run(data,value)
        return value

    def set_is_function(self,is_function):
        self.is_function = is_function

    def set_is_expression(self,is_expression):
        self.is_expression = is_expression

    def set_is_table(self,is_table):
        self.is_table = is_table

    def set_solve_table(self,solve_table):
        self.table_solver = solve_table
    def set_solve_function(self,solve_function):
        self.solve_function = solve_function
    def set_solve_expression(self,solve_expression):
        self.solve_expression = solve_expression






class ExpressionSolver:
    def run(self,expression):

        pattern = r'\@((\"([^\"]+)\")|(\'([^\']+)\'))'

        expression = re.sub(pattern,lambda match: str(self.calculator.evaluate(match[3])) if match[5] ==None else str(self.calculator.evaluate(match[5])),expression)
        return expression
    def set_calculator(self,calculator):
        self.calculator = calculator

class IsExpression:
    def run(self,value):
        pattern = r'\@((\"([^\"]+)\")|(\'([^\']+)\'))'
        expression = re.search(pattern,value)
        if expression:
            return True

        return False

class IsFunction:

    def run(self,value):
        pattern  = r'((\(([^()]|(?2))*\))(\[([^\[\]]|(?4))*\])*((?:(\.\w+(?2)?)|(?4))+))'
        if re.search(pattern,value):
            return True

        return False



class SolveFunction:
    def run(self,function_calling):
        self.single_function_solver.set_get_index_value(self.get_index)
        self.single_function_solver.set_process_condition(self.process_condition)

        self.function_solver.set_process_function_calling(self.process_function_calling)
        self.function_solver.set_single_obj_solver(self.single_function_solver)
        value_of_function = function_calling
        pattern = r'((\(([^()]|(?2))*\))(\[([^\[\]]|(?4))*\])*((?:(\.\w+(?2)?)|(?4))+))'
        matches = re.findall(pattern,value_of_function)
        while True:
            for match in matches:
                index_of_value = match[3]
                self.function_solver.set_data({'$function_name' : eval(match[1]+index_of_value)})
                evaluated_value =self.function_solver.solve('$function_name'+match[5])
                is_function = re.search(pattern,evaluated_value)
                if not is_function:
                    evaluated_value = self.get_original_type.run(evaluated_value)

                value_of_function = re.sub(re.escape(match[0]),evaluated_value,value_of_function)
            matches = re.findall(pattern,value_of_function)
            if not matches:
                break

        return value_of_function
    def set_function_solver(self,solver):
        self.function_solver = solver
    def set_function_solver(self,function_solver):
        self.function_solver  = function_solver

    def set_get_original_type(self,get):
        self.get_original_type = get

    def set_process_function_calling(self,function):
        self.process_function_calling = function

    def set_single_function_solver(self,solver):
        self.single_function_solver = solver

    def set_get_index(self,index):
        self.get_index = index

    def set_process_condition(self,condition):
        self.process_condition = condition




class IsTable:
    def run(self,value):

        return re.search(r'\$\s*<[\w\:\,\s]+>',value)
class TableSolver:


    def run(self,data,value):
        text = self.generate_text.run(data)
        text += f'$new_table_from_variable_to_table = {value};'
        resulte_text = self.go_next.process(text)

        value = re.search(r'\$new_table_from_variable_to_table\s*=\s*([^;]+);',resulte_text)[1]
        return value

    def set_generate_text(self,generator):
        self.generate_text = generator
    def set_next(self,go_next):
        self.go_next = go_next


class GenerateText:
    def run(self,dictionary):
        text = ''
        for key,value in dictionary.items():

            value = self.get_original_type.run(value)
            text += f"{key} = {value};"

        return text
    def set_get_original_type(self,get_original):
        self.get_original_type=get_original

class GetOriginalType:

    def run(self,value):
        flag = True
        try:
            value = eval(value)
            flag = True if type(value)==str else False
            value = str(value)

        except:
            flag = True

        if type(value)==str and flag:
            value = f'"{value}"'

        return value



##variable = "$x=@'1+2';$y=@'2+1';$var=@'12+223+(222+2)+sin(90)';$var2= $x+$y;$xy=($var2+$x+$y);$yx=$xy+$var2;"
##
##data= VariableHandler()
##data.set_calculator(Calculator())
##print(data.process(variable))
