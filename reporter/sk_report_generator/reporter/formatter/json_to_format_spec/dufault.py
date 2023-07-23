from ..base import IFormatter2
import regex as re


class DefaultFormat(IFormatter2):
    def __init__(self):
        self.value = None

    def handle(self, value, format_sepec, format_pattern):

        digit = re.sub(r'[,.e\+\-]','',value).isdigit()
        if digit:
            format_pattern = re.sub(r'\{value\}', str(value), format_pattern)
        else:
            format_pattern = re.sub(r'\{value\}', str(f'"{value}"'), format_pattern)


        return eval("f'"+format_pattern+"'"), format_sepec


    def set_successor(self, successor):
        pass
