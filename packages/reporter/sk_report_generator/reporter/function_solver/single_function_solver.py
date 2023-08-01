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

class SingleFunctionSOlver:
    def __init__(self):
        self.get_object_value = GetObjectValue()
        self.get_index_value = None
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




        self.floor.set_next(self.ceil)
        self.ceil.set_next(self.upper)
        self.upper.set_next(self.round)
        self.round.set_next(self.slice)
        self.slice.set_next(self.filter)
        self.slice.set_next(self.lower)
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
        self.range.set_next(self.set)

        self.set.set_next(self.foreach)
        self.foreach.set_next(self.sum)
        self.sum.set_next(self.default)



    def run(self,object_name,methods):


        pattern = r'\.(\w+)\s*(\((?:(?:[^()]+)|(?2))*\))|((?:\[[\w\"]+\])+)'
        matches = re.findall(pattern, methods)

        value = self.get_object_value.run(object_name)

        for match in matches:
            method,condition0,index = match

            condition = self.process_condition.run(condition0)
            if index!= '':
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