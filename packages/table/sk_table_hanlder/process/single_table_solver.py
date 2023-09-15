import regex as re

class SingleTableSolver:
    def __init__(self):
        self.wrapper = None
        self.mongo_controller = None
        self.remove_object_id = RemoveObjectId()
        self.array_table = ArrayTable()

        self.is_function= IsFunction()
        self.array_table.set_is_function(self.is_function)


    def run(self,data,variable):
        variable_name = variable[0]
        table_expression = variable[1]
        result = -1
        pattern = r'\$<((\w+(\:\w+))(\s*,(\w+(\:\w+)))*)>(((\w+)(\((([^()]|(?10)))*\)))\s*(->\s*(\w+(\((([^()]|(?10)))*\))))*)'
        match = re.search(pattern , table_expression)
        if match:


            table_names = [item for index,item in enumerate(match[1].split(',')) if item !='']
            self.set_primary_table(table_names[0])

            table_queries = self.get_query_list(match[7])

            if not self.is_table(data[self.primary_table]) or self.is_function.run(match[10]):
                self.array_table.set_array_alias(table_names[0])
                result =self.array_table.process(data,match[9],match[10])
                data[self.primary_table] = result
                table_queries = table_queries[1:]


            if self.is_table(data[self.primary_table]):
                self.wrapper.set_table_data(data,table_names)
                queries = self.wrapper.process_queries(table_queries)
                script = self.wrapper.query(queries)
                result = self.wrapper.evaluate(script)
                result = self.remove_object_id.run(result)

            return str(result)

        return -1

    def set_primary_table(self,alias):
        if ':' in alias:
            li = alias.split(':')
            self.primary_table = '$'+li[0]
        else:
            self.primary_table ='$'+alias


    def get_query_list(self,queries):

        queries = [item for index,item in enumerate( re.split(r'->',queries)) if item!='']

        return queries

    def set_wrapper(self,wrapper):
        self.wrapper = wrapper

    def set_mongo_controller(self,controller):
        self.mongo_controller = controller
        self.wrapper.set_mongo_controller(controller)

    def is_table(self,data):
        for item in data:
            if type(item) != dict:
                return False
            return True
    def set_function_solver(self,solver):
        self.function_solver =  solver
        self.array_table.set_function_solver(solver)

class RemoveObjectId:

    def run(self,result):
        result = re.sub(r'((\'|\")_id(\'|\")\s*\:\s*ObjectId\s*(\(([^()]|(?3))*\))(\s*,\s*)?)','',result)
        return result

class ArrayTable:
    def __init__(self):
        self.solve_function = SolveFunction()
        self.solve_function.set_get_original_type(GetOriginalType())

    def process(self,data,method,argument):

        if method =='select':




            condition = re.search(r'^\s*\(\s*(\((([^()]|(?1))*)\))',argument)
            if condition:
                is_condition= condition[2]
            else:
                is_condition = 'True'

            return_value = re.sub(r'^\s*(\()\s*(\((([^()]|(?2))*)\))\s*,','(',argument)
            value = []

            for item in data[self.array]:

                exec(f"{self.alias} = {item}")
                condition = eval(is_condition)

                if self.is_function.run(return_value):
                    return_value = re.sub(r'(\b)'+re.escape(self.alias)+r'(\b)',f"({item})",return_value)
                    return_value = self.solve_function.run(return_value)
                if condition:
                    if type(eval(return_value))==tuple:
                        value.append(eval(return_value)[0])
                    else:
                        value.append(eval(return_value))

                else:
                    if type(eval(return_value))==tuple:
                        value.append(eval(return_value)[1])

        return value

    def get_return_value(self,value,index):

        if type(value)==tuple:
            return value[index]
        else :
            return value

    def set_array_alias(self,alias):
        if ':' in alias:
            li = alias.split(':')
            self.alias = li[1]
            self.array = '$'+li[0]
        else:
            self.alias = alias
            self.array ='$'+alias

    def set_is_function(self,function):
        self.is_function = function

    def set_function_solver(self,solver):
        self.solve_function.set_function_solver(solver)

class IsFunction:

    def run(self,value):
        pattern  = r'((\(([^()]|(?2))*\))(\[([^\[\]]|(?4))*\])*((?:(\.\w+(?2)?)|(?4))+))'
        if re.search(pattern,value):
            return True

        return False



class SolveFunction:

    def run(self,function_calling):
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

    def set_get_original_type(self,get):
        self.get_original_type = get


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

