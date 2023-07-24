import regex as re

class TemplateToFormatList:
    def __init__(self):
        pass
    def run(self, template):

        format_classes = {}

        format_tags = re.findall(r'<format>([\s\S]*?)<\/format>', template)
        for tag in format_tags:
            format_class_matches = re.findall(r'((\w+)\s*=\s*({(?:[^{}]|(?3))*}))', tag)
            for format_class in format_class_matches:
                key = format_class[1]
                value = format_class[2]
                format_classes[key] = eval(value)

        return format_classes
