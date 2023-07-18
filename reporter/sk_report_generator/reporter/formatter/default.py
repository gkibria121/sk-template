from ..base import IFormatter
import regex as re


class Default(IFormatter):
    def __init__(self):
        self.value = None

    def format(self, value, format_sepec, format_pattern=''):
        return value

    def handle(self, value, format_sepec, format_pattern):

        digit = re.sub(r'[,.e\+\-]','',value).isdigit()
        if digit:
            format_pattern = re.sub(r'\{value\}', str(value), format_pattern)
        else:
            format_pattern = re.sub(r'\{value\}', str(f'"{value}"'), format_pattern)


        return eval("f'"+format_pattern+"'"), format_sepec


    def set_successor(self, successor):
        pass
