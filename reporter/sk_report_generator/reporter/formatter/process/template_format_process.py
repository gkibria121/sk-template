import regex as re

class TemplateFormatProcess:

    def __init__(self):
        pass

    def run(self,template):

        pattern = r'(\{\{(?:((?:[^{}]|(?1))*?))(?:((?:\:\:)(.*)))\}\})'
        matches = re.findall(pattern,template)
        i = 0
        form = ''
        for match in matches:
            value1 =match[0]
            value2 = match[3]
            value3 = match[2]
            form = form+f"\nc{i} = {value2}"
            replacement = re.sub(re.escape(value3),f':c{i}',value1)
            template = re.sub(re.escape(match[0]),replacement,template)
            i = i+1
        format_add = f'<format>{form}</format>'
        template= template+format_add

        return template