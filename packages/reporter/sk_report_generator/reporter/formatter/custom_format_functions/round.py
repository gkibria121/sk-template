from ..base import IFormatter

class Round(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,format_sepec):
        if 'round' in format_sepec:
            value = float(value)
            precision = int(format_sepec['round'])
            value = str(round(value,precision))





        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor