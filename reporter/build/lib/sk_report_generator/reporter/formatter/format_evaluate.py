import regex as re
from .default_format_evaluate import DefaultFormat
from .custom_format import CustomFormat
from .format_default import FormatDefault
from .process.template_to_format_list import TemplateToFormatList
class FormatEvaluate:


    def __init__(self):
        self.successor = None
        self.default_format= DefaultFormat()
        self.custom_format = CustomFormat()
        self.default = FormatDefault()
        self.template_to_format_list =TemplateToFormatList()

        self.default_format.set_next(self.custom_format)
        self.custom_format.set_next(self.default)

    def run(self,value,format_spec,template):

        format_class_list = self.template_to_format_list.run(template)
        return self.default_format.run(value,format_spec,format_class_list)






