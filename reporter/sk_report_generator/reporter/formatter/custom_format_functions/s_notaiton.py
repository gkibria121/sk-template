from ..base import IFormatter

class ScientificNotation(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,condition,format_sepec):
        if 'scientific_notation' in format_sepec:
            if format_sepec['scientific_notation'] == True:
                value = float(value)
                value = format(value,'e')
            if format_sepec['scientific_notation'] == False:
                value = float(value)
                value = format(value,'f')

        if 'scientific_precision' in format_sepec:

            if condition == None:
                value = float(value)
                value = format(value,f".{format_sepec['scientific_precision']}e")

        return self.successor.format(value,condition,format_sepec)

    def set_successor(self,successor):
        self.successor= successor