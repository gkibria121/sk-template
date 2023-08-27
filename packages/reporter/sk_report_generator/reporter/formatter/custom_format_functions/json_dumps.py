from ..base import IFormatter
import json

class Dumps(IFormatter):
    def __init__(self):
        self.value = None



    def format(self,value,format_sepec):
        if ('intent' in format_sepec) or ('dumps' in format_sepec):
            if ('dumps' not in format_sepec) or (format_sepec['dumps'] == True ):

                intent = int(format_sepec['intent']) if 'intent' in format_sepec else 4
                value = json.dumps(eval(value),indent=intent)





        return self.successor.format(value,format_sepec)

    def set_successor(self,successor):
        self.successor= successor