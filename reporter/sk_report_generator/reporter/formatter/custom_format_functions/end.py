from ..base import IFormatter
import regex as re
class End(IFormatter):
    def __init__(self):
        self.value = None


    def format(self,value,format_sepec):

        if 'end' in format_sepec:
            end = format_sepec['end']
            value = value+end
        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor
