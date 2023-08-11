import regex as re
class MongoWrapper:
    def __init__(self):
        self.mongo_controller = None
        self.primary_table = None


    def set_mongo_controller(self,controller):
        self.mongo_controller = controller

    def set_table_data(self,data, tables):
        self.mongo_controller.set_primary_table(self.get_table_placeholder(tables[0]))
        self.primary_table = self.get_table_placeholder(tables[0])
        for table in tables:
            table_name = self.get_table_name(table)
            table_placeholder = self.get_table_placeholder(table)
            self.mongo_controller.set_table_data(table_placeholder,data[table_name])




    def get_table_placeholder(self,table):

        if ':' not in table:
            return table.replace('$','')

        table_names = table.split(':')
        return table_names[1]

    def get_table_name(self,table):
        table = table if table.startswith('$') else f"${table}"

        if ':' not in table:
            return table
        tables = table.split(':')
        return tables[0]


    def query(self,queries):
        for query in queries:
            match = re.search(r'([a-zA-Z_]+)\w*(\((([^()]|(?2))*)\))',query)
            if match:
                query_name = match[1]
                query_argument = match[3]
                query_function = getattr(self.mongo_controller,query_name)
                query_function(self.process_query_argument(query_argument))


        result = self.mongo_controller.run()
        print(result)
##        exec(result)

    def process_query_argument(self,argument):
        argument_properties = argument[1:-1]

        pattern  = r"(((\'[^']+\')|(\"[^\"]+\"))\s*\:\s*([^\,]+))"

        arguments = re.sub(pattern,lambda match: match[3]+':'+self.process_field_ref(match[5]),argument_properties)

        return eval(f"{{ {arguments} }}")

    def process_field_ref(self,field):
        pattern  = r'('+self.primary_table+'\.)([\.\w]+)'
        processed_field = re.sub(pattern,lambda match: f'${match[2]}' , field )
        return self.add_fields(processed_field)  # test


    def add_fields(self,fields):
        if '+' in fields:
            field_list  =[ item.replace(' ','') for index,item in enumerate(fields.split('+'))]
            return f"{{'$add' : {field_list}}}"
        return fields





