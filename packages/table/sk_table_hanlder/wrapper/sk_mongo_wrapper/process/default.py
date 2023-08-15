class DefaultProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):

        return (name,argument)

    def set_next(self,go_next):

        self.go_next = go_next

    def set_primary_table(self,table):
        self.primary_table = table

    def set_argument_process(self,argument_processor):
        self.argument_processor = argument_processor