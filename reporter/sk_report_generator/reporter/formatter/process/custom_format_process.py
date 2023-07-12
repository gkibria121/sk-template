import regex as re
class CustomFormatProcess:



    def run(self, format_spec, format_class_list):

        matches = re.split(',', format_spec)
        condition = re.search(r'c(\(((?>[^()]+|(?1))*)\))', format_spec)

        format_spec_list = matches
        format_specs = {}
        if condition:
            condition = condition[2]
            format_spec_list = matches[1:]
        for key in format_spec_list:
            format_specs.update(format_class_list[key])

        return condition,format_specs