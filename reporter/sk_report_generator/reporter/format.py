from .base import IReporter
from .formatter.process.template_format_process import TemplateFormatProcess
from .formatter.default import Default
from .formatter.format_evaluate import FormatEvaluate
from .formatter.process.format_tag_remove import FormatTagRemover
import regex as re


class Formatter(IReporter):
    def __init__(self):
        self.successor = None
        self.default = Default()
        self.template_process = TemplateFormatProcess()
        self.remove_format_tag = FormatTagRemover()
        self.format = FormatEvaluate()


    def report(self, template):

        format_pattern = r'(\{(\{((?:[^{}]|(?2))*)\:([^{}]*)\})\})(?![}])'
        template = self.template_process.run(template)
        matches = re.findall(format_pattern, template)

        for match in matches:
            value = match[2]
            format_spec = match[3]
            replacement = self.format.run(value,format_spec,template)
            pattern = r'({)\s*' + re.escape(match[1]) + r'\s*(})'
            template = re.sub(pattern, replacement, template)

        template = self.remove_format_tag.run(template)

        return self.successor.report(template)

    def set_successor(self, successor):
        self.successor = successor





    def set_data(self, data):
        pass



