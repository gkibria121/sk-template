import regex as re

class TemplateFormatProcess:

    def __init__(self):
        self.count = 0

    def run(self,template):

        pattern = r'(\{(\{(([^{}]|(?1))*)(::(\{(([^{}]|(?1))*)\}))\})\})'

        matches = re.findall(pattern,template)
        i = 0
        form = ''
        for match in matches:
            value1 =match[0]
            value2 = match[5]
            value3 = match[4]
            form = form+f"\ncustomAutoClass{i} = {value2}"
            replacement = re.sub(re.escape(value3),f':customAutoClass{i}',value1)
            template = re.sub(re.escape(match[0]),replacement,template)
            i = i+1
        format_add = f'<format>{form}</format>'
        template= template+format_add
        return template



    def convert_into_class(self,match):

        print(match)
        return match