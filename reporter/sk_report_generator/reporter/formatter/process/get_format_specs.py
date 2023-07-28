import regex as re
class GetFormatSpecs:



    def run(self, format_spec, format_class_list,condition):

        classes = re.sub(r'(\,\s*)?(\(((?>[^()]+|(?2))*)\))(\s*\,)?','', format_spec)
        format_spec = classes.split('|') if '|' in classes else [classes,'']

        if condition:
            format_spec_list = format_spec[0].split(',')
        else:
            format_spec_list = format_spec[1].split(',')

        format_specs = {}

        for key in format_spec_list:
            if key!='':
                format_specs.update(format_class_list[key])

        return format_specs
