import regex as re
from ..base import IFormatHandler


class TypeHandler(IFormatHandler):

    def __init__(self):
        self.successor = None

    def handle(self,  format_specs, format_pattern):
        if 'base' in format_specs:

            format_pattern = re.sub(r'\{base\}', str(format_specs['base']), format_pattern)
            del format_specs['base']
        format_pattern = re.sub(r'\{base\}', '', format_pattern)

        return self.successor.handle( format_specs, format_pattern)
    def set_successor(self, successor):
        self.successor = successor
