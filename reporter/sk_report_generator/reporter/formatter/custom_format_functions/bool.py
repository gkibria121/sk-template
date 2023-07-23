from ..base import IFormatter
import regex as re
class Bool(IFormatter):
    def __init__(self):
        pass

    def format(self,value,format_sepec):

        if 'bool' in format_sepec:
            true,false = format_sepec['bool'].split('|')

            if value == 'True':
                value = true
            if value == 'False':
                value = false
        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor

