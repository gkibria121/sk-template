class GroupByProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):

        if name == 'group':
            argument_list = argument.split(',')
            argument = {'_id' : {}}

            for item in argument_list:
                key = item.split('.')[-1]
                value = item
                processed =self.argument_processor.process(f'{{"{key}" : {value}}}')
                argument['_id'].update(eval(processed))





        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next

    def set_primary_table(self,table):
        self.primary_table = table

    def set_argument_process(self,argument_processor):
        self.argument_processor = argument_processor

    def set_referece_process(self,process):
        self.reference_porcess = process
