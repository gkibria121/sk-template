import regex as re
import io
import sys

class Foreach:
    def __init__(self):
        self.get_data_from_variable =GetDataFromVariable()
        self.data = None
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):




        if method =='foreach':

            if condition !='':
                pattern = r'\(([\w,$]+)\)\s*\=\s*\>\s*(\{(([^{}]|(?2))*)\})'
                match = re.search(pattern,condition)
                result = ''

                for index,key_value in enumerate(value):
                    data = self.get_data_from_variable.run(self.data,match[1],key_value,index)
                    template = match[3]
                    report = self.reporter.generate_report(template, data)
                    result = result + report
                value = result




        return self.go_next.run(value,method,condition)

    def set_reporter(self,reporter):
        self.reporter = reporter


    def set_data(self,data):
        self.data = data


class GetDataFromVariable:

    def __init__(self):
        pass


    def run(self,data,key,value,index):
        return_value =data
        return_value.update({key : value, '$index'  : index})
        return return_value





