import regex as re
from .function.floor import Floor
from .function.upper_case import UpperCase
from .function.capitalize import Capitalize
from .function.sum import Sum
from .function.default import MethodDefault
from .function.ceil import Ceil
from .function.round import Round
from .function.slice import Slice
from .function.filter import Filter
from .function.avg import Avg
from .function.distinct import Distinct
from .function.reverse import Reverse
from .function.set import Set
from .function.min import Min
from .function.max import Max
from .function.count import Count
from .function.len import Len
from .function.lower import LowerCase
from .function.camel import CamelCase
from .function.snake import SnakeCase
from .function.range import Range
from .function.foreach import Foreach
from .get_obj_value import GetObjectValue
from .function.select import Select
from .function.index import Index
from .function.find import Find
from.function.in_array import In

from .get_index_value import GetIndexValue
from .process_condition import ProcessCondition
class SingleFunctionSOlver:
    def __init__(self):
        self.get_object_value = GetObjectValue()
        self.get_index_value =None
        self.process_condition = None

        self.floor = Floor()
        self.capitalize = Capitalize()
        self.upper = UpperCase()
        self.sum = Sum()
        self.default =MethodDefault()
        self.ceil = Ceil()
        self.round = Round()
        self.slice = Slice()
        self.filter = Filter()
        self.avg=  Avg()
        self.distinct = Distinct()
        self.reverse = Reverse()
        self.count = Count()
        self.set = Set()
        self.max = Max()
        self.min = Min()
        self.len = Len()
        self.lower = LowerCase()
        self.camel = CamelCase()
        self.snake = SnakeCase()
        self.range = Range()
        self.foreach = Foreach()
        self.select = Select()
        self.index = Index()
        self.find = Find()
        self.in_array = In()
        self.custom = CustomFunction()
        self.unittest_runner = Unittest()





        self.floor.set_next(self.ceil)
        self.ceil.set_next(self.upper)
        self.upper.set_next(self.round)
        self.round.set_next(self.slice)
        self.slice.set_next(self.filter)
        self.filter.set_next(self.lower)
        self.lower.set_next(self.avg)
        self.avg.set_next(self.distinct)
        self.distinct.set_next(self.reverse)
        self.reverse.set_next(self.max)
        self.max.set_next(self.min)
        self.min.set_next(self.count)
        self.count.set_next(self.capitalize)
        self.capitalize.set_next(self.len)
        self.len.set_next(self.camel)
        self.camel.set_next(self.snake)
        self.snake.set_next(self.range)
        self.range.set_next(self.select)
        self.select.set_next(self.index)
        self.index.set_next(self.find)
        self.find.set_next(self.custom)
        self.custom.set_next(self.in_array)
        self.in_array.set_next(self.set)

        self.set.set_next(self.foreach)
        self.foreach.set_next(self.sum)
        self.sum.set_next(self.default)



        self.unittest_runner.set_function_solver(self)


    def run(self,object_name,methods):


        pattern = r'(?:\.(\w+)\s*(\((?:(?:[^()]+)|(?2))*\)))|((?:\[[\w\"]+\])+)'
        matches = re.findall(pattern, methods)

        value = self.get_object_value.run(object_name)

        for match in matches:
            method,condition0,index = match

            condition = self.process_condition.run(condition0)
            if index!= '':
                value = value
                index_list =  [ item for index, item in enumerate( re.split(r'(?<=[\]])(?=[\[])?',index)) if item!='']

                for index in index_list:
                    value = self.get_index_value.run(value,index)

            if method != '':
                value = self.floor.run(value,method,condition)


        return str(value)

    def set_data(self, data):
        self.data = data
        self.get_object_value.set_data(data)


    def set_process_condition(self,process_condition):
        self.process_condition = process_condition

    def set_get_index_value(self,get_index_value):
        self.get_index_value = get_index_value


    def def_function(self,function_name,argument,code):
        self.custom.create(function_name,argument,code)


    def unittest(self,function_name,argument,list_of_test):

        result = self.unittest_runner.run(function_name,argument,list_of_test)
        return result


    def set_ds_solver_chain(self,chain):
        self.ds_solver_chain = chain
        self.custom.set_ds_solver_chain(self.ds_solver_chain)


class CustomFunction:
    def __init__(self):
        self.functions={}


    def create(self,name,argument,code):
        self.functions[name] = {'name' : name,'argument' : argument,'code' : code}

    def run(self,value,method,argument):

        if method in self.functions:
            function_argument =self.functions[method]['argument']
            list_of_function_argument =[item for index,item in enumerate (function_argument.split(',')) if item!='']
            list_of_argument = eval(f"[{argument}]")

            argument_variable = ''
            for i in range(len(list_of_function_argument)):
                argument_variable+= f"{list_of_function_argument[i]} = {list_of_argument[i]};"



            code = self.functions[method]['code']

            code_with_value = argument_variable+code
            output = self.ds_solver_chain.process(code_with_value)
            value = re.search(r'\$return\s*=\s*([^;]+);',output)
            if value:
                value = eval(value[1])
            else:
                value = -1



        return self.go_next.run(value,method,argument)

    def set_next(self,go_next):
        self.go_next = go_next
    def set_ds_solver_chain(self,chain):
        self.ds_solver_chain = chain

import io
import sys

class EvaluateScript:

    def run(self,script):

        code_string = script
        output_stream = io.StringIO()
        sys.stdout = output_stream
        exec(code_string)
        sys.stdout = sys.__stdout__
        captured_output = output_stream.getvalue().strip()

        return captured_output




class Unittest:

    def run(self,name,argument,list_of_test):

        result = []
        list_of_test = eval(list_of_test)
        for item in list_of_test:
            value = item["data"]
            for key,val in value.items():
                argument = re.sub(re.escape(key)+r'(?=\b)',str(val),argument)
            self.function_solver.set_data({str(value) : value})
            value = self.function_solver.run(str(value),f'.{name}{argument}')
            value = eval(value)
            if 'delta'  in item:
                value = round(value,item['delta'])
            if value == item['expected']:
                result.append({"id" : item["id"] , 'result' : 'Passed' ,'expected' : item['expected'] , 'actual' : value})
            else :
                result.append({"id" : item["id"] , 'result' : 'Faild' ,'expected' : item['expected'] , 'actual' : value})
        return result

    def set_function_solver(self,solver):
        self.function_solver = solver