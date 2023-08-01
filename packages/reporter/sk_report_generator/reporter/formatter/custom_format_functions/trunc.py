from ..base import IFormatter
import regex as re
class Trunc(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,format_sepec):
        if 'trunc' in format_sepec:
            value = str(value)
            number = re.search(r'(\d+)\.(\d+)',value)
            if number:
                int_part = number[1]
                float_part = number[2]
                precision = int(format_sepec['trunc'])
                float_part = '0' if float_part[0:precision]=='' else float_part[0:precision]
                value = f'{int_part}.{float_part}'


        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor