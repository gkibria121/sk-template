
class OrderByProcess:
    def __init__(self):
        self.go_next = None
        self.sort_object = SortObject()

    def process(self,name,argument):

        if name == 'sort':

            condition_list = argument.split(',')

            argument = self.sort_object.process(condition_list)

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next

    def set_primary_table(self,table):
        self.primary_table = table


    def set_argument_process(self,argument_processor):
        self.argument_processor = argument_processor
        self.sort_object.set_argument_process(self.argument_processor)

class SortObject:
    def __init__(self):
        self.get_order =GetOrder()

    def process(self,condition_list):

        temp = {}

        for item in condition_list:
            result = item.split(':')
            key = self.argument_processor.process(result[0]).replace(' ','').replace('"','')
            value = 1 if len(result)==1 else self.get_order.run(result[1])
            temp[key] = value
        return temp

    def set_argument_process(self,argument_processor):
        self.argument_processor = argument_processor


class GetOrder:
    def run(self,key):

        if key in ['asc','a','1',1]:
            return 1
        elif key in ['des','d','-1',-1]:
            return -1