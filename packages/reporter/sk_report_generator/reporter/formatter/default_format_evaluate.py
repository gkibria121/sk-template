import regex as re

class DefaultFormat:

    def run(self,value,format_spec,format_class_list):
        if len(format_class_list) ==0:
            value = str(value)
            digit = re.sub(r'[,.e\+\-]','',value).isdigit()
            if digit:
                f_value = eval(value)
            else:
                f_value = f'"{value}"'

            value =eval(f"format({f_value},format_spec)")

        return self.go_next.run(value,format_spec,format_class_list)

    def set_next(self,go_next):

        self.go_next = go_next