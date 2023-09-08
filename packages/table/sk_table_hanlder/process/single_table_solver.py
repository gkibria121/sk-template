import regex as re

class SingleTableSolver:
    def __init__(self):
        self.wrapper = None
        self.mongo_controller = None
        self.remove_object_id = RemoveObjectId()
        self.array_table = ArrayTable()

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

            if not self.is_table(data[self.primary_table]):
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



class RemoveObjectId:

    def run(self,result):
        result = re.sub(r'((\'|\")_id(\'|\")\s*\:\s*ObjectId\s*(\(([^()]|(?3))*\))(\s*,\s*)?)','',result)
        return result

class ArrayTable:

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




