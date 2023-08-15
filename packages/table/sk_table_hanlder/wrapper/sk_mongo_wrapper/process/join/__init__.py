import regex as re


class JoinProcess:
    def __init__(self):
        self.go_next = None

    def process(self,name,argument):
        if name == 'join':
            temp = []
            join_list = [item for index,item in enumerate(argument.split(',')) if item != '']
            for join in join_list:
                pattern = r'(\w+)\:(((?=\b)('+re.escape(self.primary_table)+r')\.([\w\.]+))|((?=\b)(\w+)\.([\w\.]+)))\s*=\s*(((?=\b)('+re.escape(self.primary_table)+r')\.([\w\.]+))|((?=\b)(\w+)\.([\w\.]+)))'
                result =  re.findall(pattern,join)
                right_table = result[0][0]
                from_table = result[0][6] if result[0][6] != '' else result[0][13]
                local_id = result[0][4] if result[0][4] != '' else result[0][11]
                foreign_id = result[0][7] if result[0][7] != '' else result[0][14]
                temp.append((from_table,right_table,local_id,foreign_id))
            argument = temp

        return self.go_next.process(name,argument)

    def set_next(self,go_next):

        self.go_next = go_next
    def set_primary_table(self,table):
        self.primary_table = table

    def set_argument_process(self,argument_processor):
        self.argument_processor = argument_processor