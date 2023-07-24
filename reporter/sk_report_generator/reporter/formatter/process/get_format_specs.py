import regex as re
class GetFormatSpecs:



    def run(self, format_spec, format_class_list):

        matches = re.split(',', format_spec)
        condition = re.search(r'(\(((?>[^()]+|(?1))*)\))', format_spec)

        format_spec_list = matches
        format_specs = {}
        if condition:
            format_spec_list = matches[1:]

        for key in format_spec_list:
            format_specs.update(format_class_list[key])

        return format_specs
