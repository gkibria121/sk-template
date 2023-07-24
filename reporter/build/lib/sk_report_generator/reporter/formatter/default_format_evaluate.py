import regex as re

class DefaultFormat:

    def run(self,value,format_spec,format_class_list):
        if len(format_class_list) ==0:
            if re.sub(r'[\s\-\.]', '', value).isdigit():
                value = int(value) if value.endswith('.0') or '.' not in value else float(value)
            value =  format(value, format_spec)

        return self.go_next.run(value,format_spec,format_class_list)

    def set_next(self,go_next):

        self.go_next = go_next