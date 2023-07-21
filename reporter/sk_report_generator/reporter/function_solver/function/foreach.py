import regex as re
import io
import sys

class Foreach:
    def __init__(self):
        self.get_data_from_variable =GetDataFromVariable()
    def set_next(self,go_next):
        self.go_next = go_next

    def run(self,value,method,condition):




        if method =='foreach':

            if condition !='':
                pattern = r'\(([\w,$]+)\)\=\>(\{(([^{}]|(?2))*)\})'
                match = re.search(pattern,condition)
                result = ''

                for index,item in enumerate(value):
                    data = self.get_data_from_variable.run(item,match[1],index)
                    template = match[3]
                    report = self.reporter.generate_report(template, data)
                    result = result + report
                value = result




        return self.go_next.run(value,method,condition)

    def set_reporter(self,reporter):
        self.reporter = reporter





class GetDataFromVariable:

    def __init__(self):
        pass


    def run(self,value,variable,index):
        return {variable : value, '$index'  : index}





