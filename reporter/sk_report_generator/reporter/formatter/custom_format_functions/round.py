from ..base import IFormatter

class Round(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,condition,format_sepec):
        if 'round' in format_sepec:
            if condition == None:
                value = float(value)
                precision = int(format_sepec['round'])
                value = str(round(value,precision))





        return self.successor.format(value,condition,format_sepec)

    def set_successor(self,successor):
        self.successor= successor